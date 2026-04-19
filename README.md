# QA Engineering Portfolio â Efrain Solivan

**Program:** TripleTen QA Engineering Apprenticeship
**Author:** Efrain Solivan | [LinkedIn](https://www.linkedin.com/in/efrain-solivan) | [GitHub](https://github.com/efrain-solivan)
**Core Skills:** Test Design Â· Bug Reporting Â· API Testing Â· SQL Â· Postman Â· Jira Â· Android Studio
**Automation Exposure:** Python Â· Selenium Â· Pytest Â· CI/CD (GitHub Actions)
**Progress:** Sprints 1â8 complete Â· Capstone upcoming (May 2026)

> Translating high-stakes operational compliance (United Airlines, Amazon) into rigorous software defect prevention.

---

## About This Portfolio

This repository compiles QA work completed across the TripleTen QA Engineering program (Sprints 1â8). Sprint work was developed inside the TripleTen LMS sandbox environment; this is an April 2026 compilation of all deliverables.

My foundation is in manual testing methodology â test case design using equivalence class and boundary value analysis, structured bug reporting, REST API validation, SQL data integrity checks, and mobile app testing. Automation is applied on top of that foundation, not in place of it.

---

## Manual QA Artifacts

### Test Cases & Bug Reports

| Sprint | Focus Area | Test Design Method | Artifact |
|--------|-----------|-------------------|----------|
| Sprint 1 | Urban Routes map UI â manual bug reporting | Exploratory + checklist | ð [Jira Board ESP1](#) |
| Sprint 2 | Address field validation â 22 test cases | EC/BV analysis | ð [Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit?usp=sharing) |
| Sprint 3 | Payment card validation | EC/BV, boundary testing | ð [Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit?usp=sharing) |
| Sprint 4 | REST API â Kits & Fast Delivery endpoints | EC/BV on request params | ð [Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit?usp=sharing) |
| Sprint 6 | Urban Lunch Android app | Mobile functionality checklist | ð [Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit?usp=sharing) |

### Postman Collection â REST API Testing (Sprint 4)

File: `postman/urban_routes_api_collection.json`

11 requests covering the Urban Routes REST API, including happy-path, edge-case, and negative tests.

```
POST /api/v1/kits        â Add items to kit (EC/BV on name length, required fields)
GET  /api/v1/kits/{id}   â Retrieve kit by ID (valid ID, invalid ID, missing ID)
POST /order/fastDelivery â Fast delivery availability (address + time edge cases)
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
| Sprint 1 | Testing Fundamentals â bug reporting, Urban Routes map UI | ð [Jira Board ESP1](#) | â Accepted |
| Sprint 2 | Test Design â address field EC/BV, 22 test cases | ð [Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit?usp=sharing) | â Accepted |
| Sprint 3 | Web App Testing â payment card EC/BV | ð [Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit?usp=sharing) | â Accepted |
| Sprint 4 | APIs â REST API validation, Kits & Fast Delivery | ð [Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit?usp=sharing) Â· ð¬ [Postman](https://github.com/efrain-solivan/TripleTen-QA-projects-ES/tree/main/postman) | â Accepted |
| Sprint 5 | Databases â SQL data integrity, Urban Routes | ðï¸ [SQL queries](#) | â Complete |
| Sprint 6 | Mobile Testing â Urban Lunch Android app checklist | ð [Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit?usp=sharing) | â Accepted |
| Sprint 7 | Python Fundamentals | â | â Complete |
| Sprint 8 | Selenium WebDriver â Urban Routes full order flow, 14 tests | ð¤ [selenium/](#) | â Complete |
| Sprint 9 | Final Project â capstone | â | â³ Upcoming |

---

### `selenium/` â Sprint 8: Urban Routes Order Flow

14 automated UI tests covering the full booking flow in the TripleTen sandbox environment.

| | |
|---|---|
| **Tests** | 14 |
| **Stack** | Python Â· Selenium WebDriver |
| **Status** | â Complete |

---

## Test Coverage Summary

| Layer | Tests | Environment |
|-------|-------|-------------|
| UI â Sandbox (Urban Routes) | 14 | TripleTen sandbox |
| **Total (automated)** | **14** | |

Manual test cases, Postman requests, and SQL queries are documented separately in the sprint artifacts above.

---

## Repository Structure

```
TripleTen-QA-projects-ES/
â
âââ .github/workflows/
â
âââ selenium/                    â Sprint 8 â Urban Routes order flow (14 tests)
â
âââ postman/                     â Sprint 4 Postman collection (11 requests)
â   âââ urban_routes_api_collection.json
â
âââ sql/                         â Sprint 5 SQL integrity queries (10 queries)
â   âââ urban_routes_data_integrity.sql
â
âââ test-cases/
â   âââ urban_routes_test_cases.md
â
âââ sprint-1/ through sprint-6/  â per-sprint artifacts, reviewer feedback & bug tables
â
âââ TEST_STRATEGY.md             â Test pyramid, marker strategy, fixture philosophy
âââ CONTRIBUTING.md              â Setup, run instructions, CI/CD notes
âââ README.md
```
