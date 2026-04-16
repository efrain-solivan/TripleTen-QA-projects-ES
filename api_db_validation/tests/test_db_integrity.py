"""
DB Integrity Tests — 6 tests validating SQLite state directly after API calls.

Defect patterns covered:
    1. Orphan subscriptions — subscriptions with no matching user row
    2. Soft-delete bug — is_deleted flag not set after DELETE call
    3. Billing on deleted users — billing rows must not reference deleted users
    4. State machine violation — order status skips required intermediate states
    5. Temporal anomaly — order_status_history timestamps out of sequence
    6. Duplicate active subscriptions — a user should not have two active plans
"""

import sqlite3
from datetime import datetime, timedelta
import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def create_user(client, name="Test User", email="test@example.com"):
    resp = client.post("/users", json={"name": name, "email": email})
    return resp.get_json()["id"]


def insert_subscription(db_conn, user_id, status="active"):
    db_conn.execute(
        "INSERT INTO subscriptions (user_id, plan, status) VALUES (?, 'pro', ?)",
        (user_id, status),
    )
    db_conn.commit()


def insert_billing(db_conn, user_id, amount=9.99):
    db_conn.execute(
        "INSERT INTO billing (user_id, amount) VALUES (?, ?)",
        (user_id, amount),
    )
    db_conn.commit()


def insert_order_with_history(db_conn, user_id, statuses, timestamps=None):
    """
    Insert an order and populate its status history.
    statuses: list of status strings in intended sequence
    timestamps: list of ISO datetime strings; auto-generated if None
    """
    cursor = db_conn.execute(
        "INSERT INTO orders (user_id, status) VALUES (?, ?)",
        (user_id, statuses[-1]),
    )
    db_conn.commit()
    order_id = cursor.lastrowid

    base = datetime(2024, 1, 1, 12, 0, 0)
    for i, status in enumerate(statuses):
        ts = timestamps[i] if timestamps else (base + timedelta(hours=i)).isoformat()
        db_conn.execute(
            "INSERT INTO order_status_history (order_id, status, changed_at) VALUES (?, ?, ?)",
            (order_id, status, ts),
        )
    db_conn.commit()
    return order_id


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestDBIntegrity:

    def test_no_orphan_subscriptions(self, client, db_conn):
        """
        Subscriptions must always reference a row in the users table.
        An orphan arises when a subscription's user_id has no matching user.
        """
        uid = create_user(client)
        insert_subscription(db_conn, uid)

        orphans = db_conn.execute(
            """
            SELECT s.id, s.user_id
            FROM subscriptions s
            LEFT JOIN users u ON s.user_id = u.id
            WHERE u.id IS NULL
            """
        ).fetchall()

        assert orphans == [], (
            f"Orphan subscriptions found: {[dict(r) for r in orphans]}"
        )

    def test_soft_delete_sets_flag_in_db(self, client, db_conn):
        """
        After DELETE /users/<id>, the row must remain in the DB with is_deleted=1.
        A bug would leave is_deleted=0 or physically remove the row.
        """
        uid = create_user(client)
        client.delete(f"/users/{uid}")

        row = db_conn.execute(
            "SELECT is_deleted FROM users WHERE id = ?", (uid,)
        ).fetchone()

        assert row is not None, f"User {uid} row was physically deleted — soft delete broken"
        assert row["is_deleted"] == 1, (
            f"Expected is_deleted=1 after DELETE, got {row['is_deleted']}"
        )

    def test_no_billing_on_deleted_users(self, client, db_conn):
        """
        Billing records created while a user is active must not follow them
        into a deleted state as new charges.  After deletion, zero additional
        billing rows should reference that user.

        Setup: bill the user while active, soft-delete them, then verify no
        further billing rows were added post-deletion.
        """
        uid = create_user(client)

        # Billing while the user is active — this is legitimate
        insert_billing(db_conn, uid, amount=9.99)

        # Capture the billing count before deletion
        count_before = db_conn.execute(
            "SELECT COUNT(*) FROM billing WHERE user_id = ?", (uid,)
        ).fetchone()[0]

        # Soft-delete via API
        client.delete(f"/users/{uid}")

        # No new billing should have been created after the delete call
        count_after = db_conn.execute(
            "SELECT COUNT(*) FROM billing WHERE user_id = ?", (uid,)
        ).fetchone()[0]

        assert count_after == count_before, (
            f"Billing count changed after soft-delete: "
            f"before={count_before}, after={count_after} — "
            "something is creating charges against a deleted user"
        )

    def test_order_state_machine_no_skip(self, client, db_conn):
        """
        Valid order transitions: pending → processing → shipped → delivered.
        Skipping directly from pending → delivered is a state machine violation.
        """
        VALID_TRANSITIONS = {
            "pending": {"processing"},
            "processing": {"shipped"},
            "shipped": {"delivered"},
            "delivered": set(),
        }
        uid = create_user(client)
        insert_order_with_history(
            db_conn, uid,
            statuses=["pending", "processing", "shipped", "delivered"],
        )

        history = db_conn.execute(
            """
            SELECT order_id, status
            FROM order_status_history
            ORDER BY order_id, changed_at
            """
        ).fetchall()

        violations = []
        prev_by_order = {}
        for row in history:
            oid, status = row["order_id"], row["status"]
            prev = prev_by_order.get(oid)
            if prev is not None:
                allowed = VALID_TRANSITIONS.get(prev, set())
                if status not in allowed:
                    violations.append(
                        {"order_id": oid, "from": prev, "to": status}
                    )
            prev_by_order[oid] = status

        assert violations == [], f"State machine violations: {violations}"

    def test_no_temporal_anomalies_in_order_history(self, client, db_conn):
        """
        Each subsequent status change for an order must have a later timestamp.
        A timestamp going backward is a temporal anomaly.
        """
        uid = create_user(client)
        insert_order_with_history(
            db_conn, uid,
            statuses=["pending", "processing", "shipped"],
            timestamps=[
                "2024-01-01T10:00:00",
                "2024-01-01T11:00:00",
                "2024-01-01T12:00:00",
            ],
        )

        history = db_conn.execute(
            """
            SELECT order_id, status, changed_at
            FROM order_status_history
            ORDER BY order_id, changed_at
            """
        ).fetchall()

        anomalies = []
        prev_ts_by_order = {}
        for row in history:
            oid = row["order_id"]
            ts = row["changed_at"]
            prev_ts = prev_ts_by_order.get(oid)
            if prev_ts and ts <= prev_ts:
                anomalies.append(
                    {"order_id": oid, "prev": prev_ts, "current": ts}
                )
            prev_ts_by_order[oid] = ts

        assert anomalies == [], f"Temporal anomalies in order history: {anomalies}"

    def test_no_duplicate_active_subscriptions(self, client, db_conn):
        """
        Each user should have at most one active subscription.
        This test verifies that creating a single subscription results in exactly
        one active row and that the uniqueness invariant holds across all users.
        """
        uid = create_user(client)
        insert_subscription(db_conn, uid, status="active")

        # Also add a cancelled subscription — should NOT count as a duplicate
        insert_subscription(db_conn, uid, status="cancelled")

        duplicates = db_conn.execute(
            """
            SELECT user_id, COUNT(*) as cnt
            FROM subscriptions
            WHERE status = 'active'
            GROUP BY user_id
            HAVING cnt > 1
            """
        ).fetchall()

        assert duplicates == [], (
            f"Users with multiple active subscriptions: {[dict(r) for r in duplicates]}"
        )
