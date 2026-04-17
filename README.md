# QA Engineering Portfolio — Efrain Solivan

**Program:** TripleTen QA Engineering Apprenticeship
**Author:** Efrain Solivan | [LinkedIn](https://www.linkedin.com/in/efrain-solivan) | [GitHub](https://github.com/efrain-solivan)
**Core Skills:** Test Design · Bug Reporting · API Testing · SQL · Postman · Jira · Android Studio
**Automation Exposure:** Python · Selenium · Pytest · CI/CD (GitHub Actions)
**Progress:** Sprints 1–8 complete · Capstone upcoming (May 2026)

> Translating high-stakes operational compliance (United Airlines, Amazon) into rigorous software defect prevention.

---

## About This Portfolio

This repository compiles QA work completed across the TripleTen QA Engineering program (Sprints 1–8). Sprint work was developed inside the TripleTen LMS sandbox environment; this is an April 2026 compilation of all deliverables.

My foundation is in manual testing methodology — test case design using equivalence class and boundary value analysis, structured bug reporting, REST API validation, SQL data integrity checks, and mobile app testing. Automation is applied on top of that foundation, not in place of it.

---

## Manual QA Artifacts

### Test Cases & Bug Reports

| Sprint | Focus Area | Test Design Method | Artifact |
|--------|-----------|-------------------|----------|
| Sprint 1 | Urban Routes map UI — manual bug reporting | Exploratory + checklist | 📋 [Jira Board ESP1](#) |
| Sprint 2 | Address field validation — 22 test cases | EC/BV analysis | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit?usp=sharing) |
| Sprint 3 | Payment card validation | EC/BV, boundary testing | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit?usp=sharing) |
| Sprint 4 | REST API — Kits & Fast Delivery endpoints | EC/BV on request params | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit?usp=sharing) |
| Sprint 6 | Urban Lunch Android app | Mobile functionality checklist | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit?usp=sharing) |

### Postman Collection — REST API Testing (Sprint 4)

File: `postman/urban_routes_api_collection.json`

11 requests covering the Urban Routes REST API, including happy-path, edge-case, and negative tests.

```
POST /api/v1/kits        — Add items to kit (EC/BV on name length, required fields)
GET  /api/v1/kits/{id}   — Retrieve kit by ID (valid ID, invalid ID, missing ID)
POST /order/fastDelivery — Fast delivery availability (address + time edge cases)
```

### SQL Data Integrity Queries (Sprint 5)

File: `sql/urban_routes_data_integrity.sql`

10 queries validating Urban Routes database integrity: orphaned records, NULL constraint violations, and referential integrity between drivers and routes tables.

```sql
-- Sample: drivers without assigned routes
SELECT d.id, d.name
FROM drivers d
LEFT JOIN routes r ON d.id = r.driver_id
WHERE r.id IS NULL;
```

### Test Case Document

File: `test-cases/urban_routes_test_cases.md`

Structured test cases for the Urban Routes application covering form validation, payment flow, and map interaction.

---

## Sprint Index

| Sprint | Topic | Artifact | Status |
|--------|-------|----------|--------|
| Sprint 1 | Testing Fundamentals — bug reporting, Urban Routes map UI | 📋 [Jira Board ESP1](#) | ✅ Accepted |
| Sprint 2 | Test Design — address field EC/BV, 22 test cases | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit?usp=sharing) | ✅ Accepted |
| Sprint 3 | Web App Testing — payment card EC/BV | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit?usp=sharing) | ✅ Accepted |
| Sprint 4 | APIs — REST API validation, Kits & Fast Delivery | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit?usp=sharing) · 📬 [Postman](https://github.com/efrain-solivan/TripleTen-QA-projects-ES/tree/main/postman) | ✅ Accepted |
| Sprint 5 | Databases — SQL data integrity, Urban Routes | 🗄️ [SQL queries](#) | ✅ Complete |
| Sprint 6 | Mobile Testing — Urban Lunch Android app checklist | 📊 [Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit?usp=sharing) | ✅ Accepted |
| Sprint 7 | Python Fundamentals | — | ✅ Complete |
| Sprint 8 | Selenium WebDriver — Urban Routes full order flow, 14 tests | 🤖 [selenium/](#) | ✅ Complete |
| Sprint 9 | Final Project — capstone | — | ⏳ Upcoming |

> ⚠️ Sprints 1–8 were completed in the TripleTen LMS sandbox environment against a controlled test application. The `ecommerce_automation/` project below targets a live production site.

---

## Automation Projects

### 🌟 Featured: Shift-Left API & DB Integrity Validation Suite

**`api_db_validation/`** — Self-Contained Flask + SQLite

This project demonstrates the ability to catch defects at the database layer before the UI is ever built — validating data contracts, constraint integrity, and API behavior from the ground up.

| | |
|---|---|
| **Tests** | 17 (11 API · 6 DB · 97% DB coverage) |
| **Stack** | Python · Flask · SQLite · Pytest |
| **CI** | GitHub Actions — runs on every push |
| **Status** | ✅ All passing |

---

### UI Automation Learning Project: Live Production SPA

**`ecommerce_automation/`** — Jomashop (Live Production Site)

Selenium + Pytest framework targeting a live e-commerce site with dynamic bot-mitigation. See `ecommerce_automation/README.md` for full technical details.

| | |
|---|---|
| **Tests** | 3 (search smoke · sort label · price sort order) |
| **Stack** | Python 3.14 · Pytest 9.0.3 · Selenium 4 · undetected-chromedriver |
| **Architecture** | Page Object Model · explicit `WebDriverWait` · zero `time.sleep()` |
| **Status** | ✅ 3 passed |

---

### `selenium/` — Sprint 8: Urban Routes Order Flow

14 automated UI tests covering the full booking flow in the TripleTen sandbox environment.

| | |
|---|---|
| **Tests** | 14 |
| **Stack** | Python · Selenium WebDriver |
| **Status** | ✅ Complete |

---

## Test Coverage Summary

| Layer | Tests | Environment |
|-------|-------|-------------|
| UI — Production (Jomashop) | 3 | Live production site |
| UI — Sandbox (Urban Routes) | 14 | TripleTen sandbox |
| API (automated) | 11 | Self-contained |
| DB (automated) | 6 | Self-contained |
| **Total (automated)** | **34** | |

Manual test cases, Postman requests, and SQL queries are documented separately in the sprint artifacts above.

---

## Repository Structure

```
TripleTen-QA-projects-ES/
│
├── .github/workflows/
│   └── tests.yml                ← CI: api_db_validation runs on every push
│
├── api_db_validation/           ← 🌟 Featured: Shift-Left API & DB (17 tests, CI)
├── ecommerce_automation/        ← UI Automation Learning Project (Jomashop)
├── selenium/                    ← Sprint 8 — Urban Routes order flow (14 tests)
│
├── postman/                     ← Sprint 4 Postman collection (11 requests)
│   └── urban_routes_api_collection.json
│
├── sql/                         ← Sprint 5 SQL integrity queries (10 queries)
│   └── urban_routes_data_integrity.sql
│
├── test-cases/
│   └── urban_routes_test_cases.md
│
├── sprint-1/ through sprint-6/  ← per-sprint artifacts, reviewer feedback & bug tables
│
├── TEST_STRATEGY.md             ← Test pyramid, marker strategy, fixture philosophy
├── CONTRIBUTING.md              ← Setup, run instructions, CI/CD notes
└── README.md
```
