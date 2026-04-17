"""
External API Tests — JSONPlaceholder
Target: https://jsonplaceholder.typicode.com (public REST API, not designed by tester)

Suite coverage (10 tests):
    GET  /users          — count, schema, nested geo fields
    GET  /users/:id      — schema validation, 404 on missing resource
    GET  /posts          — count, field shape
    GET  /posts?userId=  — filter accuracy (no leak to other users)
    POST /posts          — 201, echoed fields, generated id
    DELETE /posts/:id    — 200, empty body
    GET  /posts/:id/comments — relationship integrity, email format
    GET  /todos/:id      — boolean type check on completed field
    GET  /todos?userId=  — filter accuracy

Purpose: demonstrates testing against a system the tester did not design,
using live HTTP calls via the requests library instead of a local test client.
"""

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

class TestUsers:

    def test_get_all_users_returns_200_and_10_records(self):
        resp = requests.get(f"{BASE_URL}/users")
        assert resp.status_code == 200
        users = resp.json()
        assert isinstance(users, list), "Expected list, got non-list response"
        assert len(users) == 10, f"Expected 10 users, got {len(users)}"

    def test_get_single_user_schema_has_required_fields(self):
        resp = requests.get(f"{BASE_URL}/users/1")
        assert resp.status_code == 200
        user = resp.json()
        for field in ("id", "name", "username", "email", "address", "phone", "website", "company"):
            assert field in user, f"Missing top-level field: {field}"

    def test_user_address_contains_geo_coordinates(self):
        resp = requests.get(f"{BASE_URL}/users/1")
        assert resp.status_code == 200
        geo = resp.json()["address"]["geo"]
        assert "lat" in geo and "lng" in geo, "Geo object missing lat/lng"

    def test_nonexistent_user_returns_404(self):
        resp = requests.get(f"{BASE_URL}/users/999")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# Posts
# ---------------------------------------------------------------------------

class TestPosts:

    def test_get_all_posts_returns_100_records(self):
        resp = requests.get(f"{BASE_URL}/posts")
        assert resp.status_code == 200
        posts = resp.json()
        assert len(posts) == 100, f"Expected 100 posts, got {len(posts)}"

    def test_filter_by_user_id_returns_only_matching_posts(self):
        """No filter leak — every returned post must belong to the requested user."""
        resp = requests.get(f"{BASE_URL}/posts", params={"userId": 1})
        assert resp.status_code == 200
        posts = resp.json()
        assert len(posts) > 0, "Filter returned empty list"
        leaks = [p for p in posts if p["userId"] != 1]
        assert leaks == [], f"Filter leak — posts from other users returned: {leaks}"

    def test_create_post_returns_201_with_echoed_body_and_new_id(self):
        payload = {
            "title": "QA Automation Test Post",
            "body": "Automated test — Efrain Solivan",
            "userId": 1
        }
        resp = requests.post(f"{BASE_URL}/posts", json=payload)
        assert resp.status_code == 201
        body = resp.json()
        assert body["title"] == payload["title"], "Title not echoed in response"
        assert body["userId"] == payload["userId"], "userId not echoed in response"
        assert "id" in body, "Response missing generated id"

    def test_delete_post_returns_200_and_empty_object(self):
        resp = requests.delete(f"{BASE_URL}/posts/1")
        assert resp.status_code == 200
        assert resp.json() == {}, f"Expected empty object, got: {resp.json()}"


# ---------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------

class TestComments:

    def test_post_comments_all_reference_correct_post_id(self):
        """Relationship integrity — no comment should belong to a different post."""
        resp = requests.get(f"{BASE_URL}/posts/1/comments")
        assert resp.status_code == 200
        comments = resp.json()
        assert len(comments) > 0, "No comments returned for post 1"
        leaks = [c for c in comments if c["postId"] != 1]
        assert leaks == [], f"Comments referencing wrong postId: {leaks}"

    def test_every_comment_has_valid_email_field(self):
        resp = requests.get(f"{BASE_URL}/posts/1/comments")
        assert resp.status_code == 200
        for comment in resp.json():
            assert "email" in comment, f"Comment {comment.get('id')} missing email"
            assert "@" in comment["email"], f"Invalid email format: {comment['email']}"


# ---------------------------------------------------------------------------
# Todos
# ---------------------------------------------------------------------------

class TestTodos:

    def test_todo_completed_field_is_boolean(self):
        resp = requests.get(f"{BASE_URL}/todos/1")
        assert resp.status_code == 200
        todo = resp.json()
        for field in ("userId", "id", "title", "completed"):
            assert field in todo, f"Missing field: {field}"
        assert isinstance(todo["completed"], bool), (
            f"'completed' should be bool, got {type(todo['completed'])}"
        )

    def test_filter_todos_by_user_id_returns_only_matching_records(self):
        """No filter leak — every returned todo must belong to the requested user."""
        resp = requests.get(f"{BASE_URL}/todos", params={"userId": 1})
        assert resp.status_code == 200
        todos = resp.json()
        assert len(todos) > 0, "Filter returned empty list"
        leaks = [t for t in todos if t["userId"] != 1]
        assert leaks == [], f"Filter leak — todos from other users returned: {leaks}"
