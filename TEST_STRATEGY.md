# Test Strategy — TripleTen QA Portfolio

**Author:** Efrain Solivan
**Last updated:** April 2026

This document explains the testing philosophy, architectural decisions, and layer structure used across this portfolio. It answers the question hiring managers and senior engineers ask in interviews: *"How do you think about testing — not just how do you write tests?"*

---

## Test Pyramid

This portfolio is organized around the classic test pyramid — many fast, isolated checks at the base, fewer slow end-to-end tests at the top.

```
        ▲
       /E\          UI / End-to-End (Selenium)
      /───\         Slow · Brittle if overused · High confidence when passing
     / API \        API response validation (Postman + pytest)
    /───────\       Medium speed · Low brittleness · Catches contract breaks
   / DB Layer \     Database integrity (pytest + SQLite direct connection)
  /─────────────\   Fast · Zero external deps · Catches what APIs hide
 / Manual & Design\ Test design, exploratory, mobile (Sprints 1–6)
/─────────────────── Foundation of every automated layer
```

### Why this matters in practice

API tests pass; DB tests fail. That gap is where real bugs live. Sprint 4 found 11 defects where the Urban Routes API returned `200 OK` while the underlying data was corrupt or the business rule was violated. The `api_db_validation/` suite was built specifically to prove that API-level assertions are not sufficient.

---

## Test Layer Breakdown

### Layer 1 — Test Design (Sprints 1–4, 6)
Manual test case design using Equivalence Class (EC) partitioning and Boundary Value Analysis (BVA). Every automated test in this repo traces back to a manually designed test case. Automation without design produces tests that check implementation details, not requirements.

**Key artifacts:** Sprint 2 (22 EC/BV test cases), Sprint 3 (payment card boundary tests), Sprint 4 (API test cases)

### Layer 2 — Database Integrity (`api_db_validation/tests/test_db_integrity.py`)
Six tests that connect directly to SQLite after API calls and verify row-level state. This layer exists because:

- APIs can return success codes while writing invalid data
- Soft-delete bugs (flag not set), orphan records, and billing anomalies are invisible to the API consumer
- State machine violations and temporal anomalies require inspecting sequences of rows — not single responses

**Runs in CI on every push.** Zero external dependencies.

### Layer 3 — API Response Validation (`api_db_validation/tests/test_api_responses.py`, `postman/`)
Nine pytest tests covering POST/GET/DELETE happy paths, missing fields, duplicate emails, and soft-delete behavior via HTTP. The Postman collection covers the same Urban Routes sandbox API with 11 requests including automated `pm.test()` assertions.

**Runs in CI on every push** (pytest suite). Postman collection runs locally.

### Layer 4 — UI Automation (`selenium/`, `ecommerce_automation/`)
Two Selenium frameworks targeting different environments:

- `selenium/` — 14 tests against the TripleTen sandbox (Urban Routes full order flow, Comfort tariff)
- `ecommerce_automation/` — 3 tests against live Jomashop.com (search, sort, price validation)

UI tests are the most expensive to maintain. Both frameworks use Page Object Model to isolate selectors from test logic, so markup changes require editing one file, not every test.

---

## Fixture Strategy

All test state is isolated per test via `conftest.py` fixtures. No test depends on the side effects of another.

**`api_db_validation/conftest.py`** drops and re-creates all tables before each test via a `client` fixture. This means:
- Tests can run in any order
- A failing test does not contaminate the next test's data
- No `setUp`/`tearDown` boilerplate in test files — the fixture handles it

**`selenium/conftest.py`** and **`ecommerce_automation/conftest.py`** both scope the browser session to the test session (not per test) for performance. A screenshot-on-failure hook captures browser state at the exact moment of failure without requiring a re-run.

---

## Marker Strategy

Tests are tagged with markers that control execution scope:

| Marker | Intent | When to run |
|--------|--------|-------------|
| `smoke` | Critical path only — minimum viable pass | Every push, pre-merge |
| `full` | Complete happy path regression | Pre-release, scheduled |
| `negative` | Error conditions and edge cases | Pre-release, when modifying validation logic |
| `flaky` | Tests sensitive to timing or network | Isolated, never in CI gate |

Running `pytest -m smoke` gives fast feedback (~2 min) without blocking on the full suite.

---

## CI/CD Design

The GitHub Actions workflow (`.github/workflows/tests.yml`) runs two jobs:

**Job 1 — `api-db-tests` (always runs):** The `api_db_validation` suite requires only Python and pip. No browser, no sandbox server, no secrets. It runs on every push and pull request. Coverage is measured with `pytest-cov` and the XML report is uploaded as an artifact.

**Job 2 — `selenium-smoke` (opt-in):** Selenium tests require the TripleTen sandbox URL (a time-limited environment). This job only runs when the `SELENIUM_ENABLED` repository variable is set to `true`. Failure screenshots are uploaded as artifacts automatically.

This design keeps CI green and fast by default, while making the full UI suite available when the environment is active.

---

## What this portfolio does not yet cover

Being direct about gaps is part of good QA thinking:

- **Performance testing** — no load or stress tests (Locust, k6, or pytest-benchmark)
- **Accessibility testing** — no a11y assertions (axe-core, pytest-axe)
- **Visual regression** — no screenshot comparison (Percy, Playwright visual)
- **Mobile automation** — Sprint 6 is manual-only; no Appium framework
- **Cross-browser** — both Selenium suites use Chrome only

These are honest gaps, not oversights. The portfolio prioritizes depth over breadth — a thorough multi-layer approach on two well-understood systems rather than shallow coverage across many tools.
