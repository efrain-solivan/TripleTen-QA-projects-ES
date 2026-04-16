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

### API Response Tests (`test_api_responses.py`) — 11 tests

| # | Class | Test | Assertion |
|---|-------|------|-----------|
| 1 | `TestCreateUser` | POST valid input | Returns `201` |
| 2 | `TestCreateUser` | POST response fields | Body contains `id`, `name`, `email`, `is_deleted`, `created_at` |
| 3 | `TestCreateUser` | POST missing name | Returns `400` with `error` key |
| 4 | `TestCreateUser` | POST missing email | Returns `400` |
| 5 | `TestCreateUser` | POST duplicate email | Returns `409` |
| 6 | `TestListUsers` | GET empty DB | Returns `200`, empty list |
| 7 | `TestListUsers` | GET after create | Created user appears in list |
| 8 | `TestListUsers` | GET after delete | Deleted user excluded |
| 9 | `TestDeleteUser` | DELETE valid user | Returns `200` |
| 10 | `TestDeleteUser` | DELETE non-existent | Returns `404` |
| 11 | `TestDeleteUser` | DELETE already deleted | Returns `404` |

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

Expected output: **17 passed** (11 API + 6 DB) with **97% code coverage**

```
platform linux -- Python 3.10.12, pytest-9.0.3
collected 17 items

tests/test_api_responses.py::TestCreateUser::test_returns_201_on_valid_input PASSED
tests/test_api_responses.py::TestCreateUser::test_response_contains_expected_fields PASSED
tests/test_api_responses.py::TestCreateUser::test_returns_400_when_name_missing PASSED
tests/test_api_responses.py::TestCreateUser::test_returns_400_when_email_missing PASSED
tests/test_api_responses.py::TestCreateUser::test_returns_409_on_duplicate_email PASSED
tests/test_api_responses.py::TestListUsers::test_returns_200_with_empty_list PASSED
tests/test_api_responses.py::TestListUsers::test_returns_created_user_in_list PASSED
tests/test_api_responses.py::TestListUsers::test_deleted_user_excluded_from_list PASSED
tests/test_api_responses.py::TestDeleteUser::test_returns_200_on_valid_delete PASSED
tests/test_api_responses.py::TestDeleteUser::test_returns_404_on_nonexistent_user PASSED
tests/test_api_responses.py::TestDeleteUser::test_returns_404_when_deleting_already_deleted_user PASSED
tests/test_db_integrity.py::TestDBIntegrity::test_no_orphan_subscriptions PASSED
tests/test_db_integrity.py::TestDBIntegrity::test_soft_delete_sets_flag_in_db PASSED
tests/test_db_integrity.py::TestDBIntegrity::test_no_billing_on_deleted_users PASSED
tests/test_db_integrity.py::TestDBIntegrity::test_order_state_machine_no_skip PASSED
tests/test_db_integrity.py::TestDBIntegrity::test_no_temporal_anomalies_in_order_history PASSED
tests/test_db_integrity.py::TestDBIntegrity::test_no_duplicate_active_subscriptions PASSED

Name              Stmts   Miss  Cover
-----------------------------------------------
app/__init__.py       0      0   100%
app/app.py           59      2    97%
-----------------------------------------------
TOTAL                59      2    97%

17 passed in 0.95s
```

---

## Key Design Decisions

- **Isolated DB per test** — `conftest.py` drops and re-creates all tables before
  each test, so tests never interfere with each other.
- **No mocking** — the DB integrity tests use a real SQLite connection to assert
  actual row state, not API response shape.
- **Soft delete** — preserves audit history while preventing deleted users from
  appearing in API responses or accruing new charges.
