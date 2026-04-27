# Urban Routes / Urban Lunch Ecosystem — QA Engineering Portfolio

**Program:** TripleTen QA Engineering Apprenticeship
**Projects:** Urban Routes (Ride-Hailing) · Urban Lunch (Food Delivery)
**Author:** Efrain Solivan
**Started:** July 2025 | **Progress:** Sprints 1–8 complete (89% of program)

---

## About This Repository

This repo documents all QA work completed in the TripleTen QA Engineering program across two applications: the Urban Routes ride-hailing platform and the Urban Lunch food delivery app. Each sprint has its own folder with a detailed README, links to live project artifacts (Google Sheets, Jira), and relevant code files.

> ⚠️ **Note:** All testing was conducted in the TripleTen sandbox environment. This does not represent work in a production environment or at a real company.

---

## Test Artifact Summary

| Artifact Type | Count |
|---|---|
| Manual Test Cases | 22 |
| Selenium E2E Tests | 9 |
| Postman API Endpoints | 11 |
| SQL Integrity Queries | 10 |
| Mobile Test Matrix (cases) | 51 |
| **Total** | **103** |

Defects logged in Jira: **40** (3 Critical · 24 High · 9 Medium · 4 Low)
Cross-browser issues found: **15+** (Chrome · Firefox · Edge)

---

## Sprint Index

| Sprint | Topic | Project | Artifact | Status |
|---|---|---|---|---|
| [Sprint 1](sprint-1) | Testing Fundamentals | Manual testing & bug reporting — Urban Routes map UI | [Jira Board ESP1](https://rainsol.atlassian.net/jira/software/projects/ESP1/boards/1) | ✅ Accepted |
| [Sprint 2](sprint-2) | Test Design & Documentation | Address field test design (EC/BV, test cases) | [Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit) | ✅ Accepted |
| [Sprint 3](sprint-3) | Testing Web Applications | Payment card validation (EC/BV, test cases) | [Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit) · [Jira ESP3](https://rainsol.atlassian.net/jira/software/projects/ESP3/boards/1) | ✅ Accepted |
| [Sprint 4](sprint-4) | APIs | REST API testing — Kits & Fast Delivery endpoints | [Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit) · [Postman](postman/urban_routes_api_collection.json) | ✅ Accepted |
| [Sprint 5](sprint-5) | Understanding Databases | SQL — data integrity queries | [SQL file](sql/urban_routes_data_integrity.sql) | ✅ Complete |
| [Sprint 6](sprint-6) | Testing Mobile Applications | Mobile checklist — Urban Lunch Android app | [Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit) | ✅ Accepted |
| Sprint 7 | Python | ✅ Accepted | — | ✅ Accepted |
| Sprint 8 | Browser Automation | Selenium WebDriver — 9 E2E tests scripted (full order flow) | [Selenium](selenium/test_urban_routes.py) | ✅ Accepted |
| Sprint 9 | Final Project | Applied Testing — capstone | — | ⏳ Upcoming |

---

## Repository Structure

```
TripleTen-QA-projects-ES/
├── sprint-1/             # Manual testing & Jira bug reports
├── sprint-2/             # Test design: address fields (Google Sheets)
├── sprint-3/             # Test design: card validation (Google Sheets)
├── sprint-4/             # API testing: kits & fast delivery (Sheets + Postman)
├── sprint-5/             # SQL: data integrity queries
├── sprint-6/             # Mobile testing checklist (Google Sheets)
├── postman/
│   └── urban_routes_api_collection.json
├── selenium/
│   └── test_urban_routes.py  # 9 E2E tests (route, booking, payment, extras)
├── sql/
│   └── urban_routes_data_integrity.sql
├── test-cases/
    └── urban_routes_test_cases.md
```

## Tech Stack

| Area | Tools |
|---|---|
| Manual Testing | Jira (ESP1, ESP3), test case templates, exploratory testing |
| Test Design | Equivalence classes, boundary value analysis, Google Sheets |
| API Testing | Postman (REST: GET/POST, status codes, response schema) |
| Database | PostgreSQL / SQL (JOINs, aggregates, CASE WHEN, subqueries) |
| Mobile Testing | Android Studio Emulator, Android app testing |
| Cross-Browser Testing | Chrome · Firefox · Edge (15+ issues documented) |
| UI Automation | Python, Pytest, Selenium WebDriver 4, ChromeDriver, Page Object Model |
| Defect Tracking | Jira (projects ESP1, ESP3) |

---

## Defect Summary (All Sprints)

| Category | Total | Critical | High | Medium | Low |
|---|---|---|---|---|---|
| Map & Address UI (S1) | 10 | 0 | 1 | 5 | 4 |
| Card Validation (S3) | 10 | 1 | 8 | 1 | 0 |
| API — Kits (S4) | 11 | 0 | 10 | 1 | 0 |
| API — Fast Delivery (S4) | 3 | 1 | 2 | 0 | 0 |
| Mobile — Urban Lunch (S6) | 6 | 1 | 3 | 2 | 0 |
| **Total** | **40** | **3** | **24** | **9** | **4** |

---

*Each sprint folder contains a full project README with tools used, what was tested, key findings, and links to all artifacts.*
