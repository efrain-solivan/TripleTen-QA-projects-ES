# API & DB Integrity Validation Suite

A self-contained Flask + SQLite project demonstrating two complementary test
layers: **API response validation** and **direct database integrity checks**.

---

## Project Structure

```
api_db_validation/
├── app/
│   ├── __init__.py
│   ├── app.py          # Flask REST API
│   └── schema.sql      # SQLite schema
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures (fresh DB per test)
│   ├── test_api_responses.py   # 9 API-level tests
│   └── test_db_integrity.py    # 6 DB integrity tests
├── requirements.txt
└── README.md
```

---

## API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/users`         | Create a user            |
| GET    | `/users`         | List all active users    |
| DELETE | `/users/<id>`    | Soft-delete a user       |

**Soft-delete** means `DELETE` sets `is_deleted = 1` — the row is never physically removed.

---

## Test Coverage

### API Response Tests (`test_api_responses.py`) — 9 tests

| # | Test | Assertion |
|---|------|-----------|
| 1 | POST valid input | Returns `201` |
| 2 | POST response fields | Body contains `id`, `name`, `email`, `is_deleted`, `created_at` |
| 3 | POST missing name | Returns `400` with `error` key |
| 4 | POST missing email | Returns `400` |
| 5 | POST duplicate email | Returns `409` |
| 6 | GET empty DB | Returns `200`, empty list |
| 7 | GET after create | Created user appears in list |
| 8 | GET after delete | Deleted user excluded |
| 9 | DELETE valid user | Returns `200` |
| 10 | DELETE non-existent | Returns `404` |
| 11 | DELETE already deleted | Returns `404` |

> Note: the test file contains 9 test methods across 3 classes; rows 10–11 are within `TestDeleteUser`.

### DB Integrity Tests (`test_db_integrity.py`) — 6 tests

| # | Defect Pattern | What Is Verified |
|---|---------------|-----------------|
| 1 | Orphan subscriptions | No `subscriptions` row exists without a matching `users` row |
| 2 | Soft-delete bug | After `DELETE /users/<id>`, `is_deleted = 1` in DB |
| 3 | Billing on deleted users | No `billing` row references a soft-deleted user |
| 4 | State machine violation | Order status transitions follow: `pending → processing → shipped → delivered` |
| 5 | Temporal anomaly | Each order status change has a strictly later timestamp than the previous |
| 6 | Duplicate active subscriptions | A user cannot have more than one `active` subscription |

---

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests from the api_db_validation/ directory
cd api_db_validation
pytest tests/ -v
```

Expected output: **15 passed**

---

## Key Design Decisions

- **Isolated DB per test** — `conftest.py` drops and re-creates all tables before
  each test, so tests never interfere with each other.
- **No mocking** — the DB integrity tests use a real SQLite connection to assert
  actual row state, not API response shape.
- **Soft delete** — preserves audit history while preventing deleted users from
  appearing in API responses or accruing new charges.
