"""
API Response Tests — 9 tests covering status codes, JSON body shape, and edge cases.

Suite coverage:
    POST /users  — happy path, missing fields, duplicate email
    GET  /users  — empty list, populated list, excludes deleted
    DELETE /users/<id> — happy path, already deleted, non-existent id
"""

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def create_user(client, name="Alice", email="alice@example.com"):
    return client.post("/users", json={"name": name, "email": email})


# ---------------------------------------------------------------------------
# POST /users
# ---------------------------------------------------------------------------

class TestCreateUser:
    def test_returns_201_on_valid_input(self, client):
        resp = create_user(client)
        assert resp.status_code == 201

    def test_response_contains_expected_fields(self, client):
        resp = create_user(client)
        body = resp.get_json()
        for field in ("id", "name", "email", "is_deleted", "created_at"):
            assert field in body, f"Missing field: {field}"

    def test_returns_400_when_name_missing(self, client):
        resp = client.post("/users", json={"email": "x@example.com"})
        assert resp.status_code == 400
        assert "error" in resp.get_json()

    def test_returns_400_when_email_missing(self, client):
        resp = client.post("/users", json={"name": "Bob"})
        assert resp.status_code == 400

    def test_returns_409_on_duplicate_email(self, client):
        create_user(client)
        resp = create_user(client)  # same email, second call
        assert resp.status_code == 409
        assert "error" in resp.get_json()


# ---------------------------------------------------------------------------
# GET /users
# ---------------------------------------------------------------------------

class TestListUsers:
    def test_returns_200_with_empty_list(self, client):
        resp = client.get("/users")
        assert resp.status_code == 200
        assert resp.get_json() == []

    def test_returns_created_user_in_list(self, client):
        create_user(client, name="Carol", email="carol@example.com")
        resp = client.get("/users")
        assert resp.status_code == 200
        users = resp.get_json()
        assert len(users) == 1
        assert users[0]["email"] == "carol@example.com"

    def test_deleted_user_excluded_from_list(self, client):
        create_resp = create_user(client, name="Dave", email="dave@example.com")
        uid = create_resp.get_json()["id"]
        client.delete(f"/users/{uid}")
        resp = client.get("/users")
        emails = [u["email"] for u in resp.get_json()]
        assert "dave@example.com" not in emails


# ---------------------------------------------------------------------------
# DELETE /users/<id>
# ---------------------------------------------------------------------------

class TestDeleteUser:
    def test_returns_200_on_valid_delete(self, client):
        uid = create_user(client).get_json()["id"]
        resp = client.delete(f"/users/{uid}")
        assert resp.status_code == 200
        assert resp.get_json()["id"] == uid

    def test_returns_404_on_nonexistent_user(self, client):
        resp = client.delete("/users/99999")
        assert resp.status_code == 404

    def test_returns_404_when_deleting_already_deleted_user(self, client):
        uid = create_user(client).get_json()["id"]
        client.delete(f"/users/{uid}")            # first delete
        resp = client.delete(f"/users/{uid}")     # second delete
        assert resp.status_code == 404
