"""
Shared pytest fixtures for API and DB integrity tests.

Design:
- Each test gets a fresh in-memory SQLite database via DB_PATH env override.
- The Flask test client is scoped to the function so every test is isolated.
"""

import os
import sqlite3
import tempfile
import pytest

# Point app at a temp file before importing, so init_db() uses the right path.
_tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_tmp.close()
os.environ["DB_PATH"] = _tmp.name

from app.app import app as flask_app, init_db  # noqa: E402  (must follow env set)


@pytest.fixture(autouse=True)
def fresh_db():
    """
    Before every test: wipe and re-apply the schema so the DB is clean.
    After every test: nothing extra needed (next fixture call re-wipes).
    """
    db_path = os.environ["DB_PATH"]
    # Drop all tables by re-connecting and running the schema fresh
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = OFF")
    # Exclude SQLite internal tables (sqlite_sequence, sqlite_stat*, etc.)
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    )
    tables = [row[0] for row in cursor.fetchall()]
    for t in tables:
        conn.execute(f"DROP TABLE IF EXISTS {t}")
    conn.commit()
    conn.close()

    # Re-apply schema
    with flask_app.app_context():
        init_db()

    yield


@pytest.fixture
def client(fresh_db):
    """Flask test client bound to the cleaned database."""
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c


@pytest.fixture
def db_conn():
    """
    Raw SQLite connection for DB integrity assertions.
    Yields the connection; caller must NOT commit — read-only use only.
    """
    db_path = os.environ["DB_PATH"]
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    yield conn
    conn.close()
