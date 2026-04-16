"""
Flask REST API — User management backed by SQLite.
Endpoints: POST /users, GET /users, DELETE /users/<id>

Design notes:
- Soft-delete: DELETE sets is_deleted=1, does not remove the row.
- Schema is auto-applied on startup from schema.sql.
"""

import os
import sqlite3
from flask import Flask, jsonify, request, g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.environ.get("DB_PATH", os.path.join(BASE_DIR, "users.db"))
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

app = Flask(__name__)


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------

def get_db():
    """Return (and cache on g) a SQLite connection for the current request."""
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Apply schema.sql to a fresh or existing database."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        with open(SCHEMA_PATH, "r") as f:
            conn.executescript(f.read())


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.post("/users")
def create_user():
    """
    Create a new user.
    Body: {"name": str, "email": str}
    Returns 201 with the created user, or 400/409 on bad input / duplicate email.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()

    if not name or not email:
        return jsonify({"error": "Both 'name' and 'email' are required"}), 400

    db = get_db()
    try:
        cursor = db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email),
        )
        db.commit()
        user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        return jsonify({"error": f"Email '{email}' is already registered"}), 409

    row = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return jsonify(dict(row)), 201


@app.get("/users")
def list_users():
    """
    Return all non-deleted users.
    Returns 200 with a list (possibly empty).
    """
    db = get_db()
    rows = db.execute(
        "SELECT * FROM users WHERE is_deleted = 0 ORDER BY id"
    ).fetchall()
    return jsonify([dict(r) for r in rows]), 200


@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    """
    Soft-delete a user by setting is_deleted=1.
    Returns 200 on success, 404 if the user does not exist or is already deleted.
    """
    db = get_db()
    row = db.execute(
        "SELECT * FROM users WHERE id = ? AND is_deleted = 0",
        (user_id,),
    ).fetchone()

    if row is None:
        return jsonify({"error": f"User {user_id} not found"}), 404

    db.execute(
        "UPDATE users SET is_deleted = 1 WHERE id = ?",
        (user_id,),
    )
    db.commit()
    return jsonify({"message": f"User {user_id} deleted", "id": user_id}), 200


# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------

with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
