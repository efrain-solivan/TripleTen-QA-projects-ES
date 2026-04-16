# QA Engineering Portfolio — Efrain Solivan

**Program:** TripleTen QA Engineering Apprenticeship
**Author:** Efrain Solivan | [LinkedIn](https://www.linkedin.com/in/efrain-solivan) | [GitHub](https://github.com/efrain-solivan)
**Stack:** Python · Selenium · Pytest · Postman · SQL · Jira · Android Studio
**Progress:** Sprints 1–8 complete · Capstone upcoming (May 2026)

[![QA Test Suite](https://github.com/efrain-solivan/TripleTen-QA-projects-ES/actions/workflows/tests.yml/badge.svg)](https://github.com/efrain-solivan/TripleTen-QA-projects-ES/actions/workflows/tests.yml)

---

## Test Suite Summary

| Framework | Tests | Type | Environment | Status |
|-----------|------:|------|-------------|--------|
| [ecommerce_automation/](./ecommerce_automation/) | 3 | UI — Live production site (Jomashop) | Windows · Python 3.14 · Chrome | ✅ 3 passed |
| [selenium/](./selenium/) | 14 | UI — Full order flow (Urban Routes) | TripleTen sandbox | ✅ Complete |
| [api_db_validation/](./api_db_validation/) — API | 11 | REST API response validation | Self-contained Flask/SQLite | ✅ 11 passed |
| [api_db_validation/](./api_db_validation/) — DB | 6 | Database integrity checks · 97% coverage | Self-contained Flask/SQLite | ✅ 6 passed |
| **Total** | **34** | **Multi-layer: UI · API · DB** | | **All passing** |

> CI runs the `api_db_validation` suite (15 tests) on every push — zero external dependencies required.
> Selenium and ecommerce suites run locally against their respective environments.

---

## 🌟 Featured: Production UI Automation

**Project:** Live E-Commerce Search & Sort Validation — [Jomashop.com](https://www.jomashop.com)
**Folder:** [`ecommerce_automation/`](./ecommerce_automation/)

Unlike the sandbox sprint projects below, this framework runs against a real production site with active bot detection and a live SPA DOM.

| What | How |
|------|-----|
| **Language & Framework** | Python 3.14 · Pytest 9.0.3 · Selenium 4 |
| **Bot detection bypass** | `undetected-chromedriver` defeats PerimeterX (active on Jomashop) |
| **Architecture** | Page Object Model · explicit `WebDriverWait` · zero `time.sleep()` |
| **Stale DOM fix** | JavaScript atomic extraction eliminates `StaleElementReferenceException` on SPA re-renders |
| **Sort validation** | 8-product sample · `min < max` guard prevents vacuous pass on uniform prices |
| **Result** | `$5.99 ≤ $5.99 ≤ $5.99 ≤ $6.99 ≤ $6.99 ≤ $6.99 ≤ $6.99 ≤ $6.99` ✓ |

```
platform win32 -- Python 3.14.2, pytest-9.0.3, pluggy-1.6.0
collected 3 items

tests/test_search_filter.py::test_search_returns_results
  [PASS] Search loaded. First 3 prices: [19.99, 19.99, 19.99]
PASSED
tests/test_search_filter.py::test_sort_label_updates_to_price_low_to_high
  [PASS] Sort applied. URL: https://www.jomashop.com/search?q=Arabic%20fragrances&sortBy=productionM2_default_products_price_default_asc
PASSED
tests/test_search_filter.py::test_price_sort_order_ascending[8]
  Prices after sort (8 products): [5.99, 5.99, 5.99, 6.99, 6.99, 6.99, 6.99, 6.99]
  [PASS] $5.99 <= $5.99 <= $5.99 <= $6.99 <= $6.99 <= $6.99 <= $6.99 <= $6.99
PASSED

3 passed in 31.23s
```

---

## Sprint Index

| Sprint | Topic | Project | Artifact | Status |
|--------|-------|---------|----------|--------|
| Sprint 1 | Testing Fundamentals | Manual testing & bug reporting — Urban Routes map UI | 📋 [Jira Board ESP1](https://rainsol.atlassian.net/jira/software/projects/ESP1/boards/1) | ✅ Accepted |
| Sprint 2 | Test Design & Documentation | Address field test design — EC/BV, 22 test cases | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit) | ✅ Accepted |
| Sprint 3 | Testing Web Applications | Payment card validation — EC/BV, boundary testing | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit) | ✅ Accepted |
| Sprint 4 | APIs | REST API testing — Kits & Fast Delivery endpoints | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit) · 📬 [Postman](postman/) | ✅ Accepted |
| Sprint 5 | Understanding Databases | SQL — Urban Routes data integrity validation | 🗄️ [SQL queries](sql/) | ✅ Complete |
| Sprint 6 | Testing Mobile Applications | Mobile checklist — Urban Lunch Android app | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit) | ✅ Accepted |
| Sprint 7 | Python | Python scripting for QA automation | — | ✅ Complete |
| Sprint 8 | Browser Automation | Selenium WebDriver — Urban Routes full order flow | 🤖 [selenium/](selenium/) | ✅ Complete |
| Sprint 9 | Final Project | Applied Testing — capstone | — | ⏳ Upcoming |

> ⚠️ Sprints 1–8 were completed in the TripleTen sandbox environment against a test application. The `ecommerce_automation/` project above targets a live production site.

---

## Repository Structure

```text
TripleTen-QA-projects-ES/
│
├── .github/workflows/
│   └── tests.yml                ← CI: api_db_validation runs on every push
│
├── ecommerce_automation/        ← 🌟 Live Production Framework (Jomashop)
│   ├── conftest.py              ← undetected_chromedriver session fixture
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── pages/
│   │   └── search_page.py      ← Page Object Model
│   ├── tests/
│   │   └── test_search_filter.py
│   └── utils/
│       └── wait_helpers.py     ← explicit WebDriverWait utilities
│
├── selenium/                    ← Sprint 8 — Urban Routes order flow (14 tests)
│   ├── conftest.py
│   ├── pages/
│   │   └── urban_routes_page.py
│   └── test_urban_routes.py
│
├── api_db_validation/           ← Self-contained Flask + SQLite (15 tests, runs in CI)
│   ├── app/
│   ├── tests/
│   │   ├── test_api_responses.py   ← 9 API tests
│   │   └── test_db_integrity.py    ← 6 DB integrity tests
│   └── requirements.txt
│
├── postman/                     ← Sprint 4 Postman collection (11 requests)
│   ├── urban_routes_api_collection.json
│   └── README.md
│
├── sql/                         ← Sprint 5 SQL integrity queries (10 queries)
│   ├── urban_routes_data_integrity.sql
│   └── README.md
│
├── test-cases/
│   └── urban_routes_test_cases.md
│
├── sprint-1/ through sprint-6/  ← per-sprint READMEs with reviewer feedback & bug tables
│
├── TEST_STRATEGY.md             ← Test pyramid, marker strategy, fixture philosophy
├── CONTRIBUTING.md              ← Setup, run instructions, CI/CD notes
└── README.md
```
