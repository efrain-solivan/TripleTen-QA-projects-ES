# Urban Routes / Urban Lunch Ecosystem â QA Engineering Portfolio

**Program:** TripleTen QA Engineering Apprenticeship
**Projects:** Urban Routes (Ride-Hailing) Â· Urban Lunch (Food Delivery)
**Author:** Efrain Solivan
**Started:** July 2025 | **Progress:** Sprints 1â8 complete (89% of program)

---

## About This Repository

This repo documents all QA work completed in the TripleTen QA Engineering program across two applications: the Urban Routes ride-hailing platform and the Urban Lunch food delivery app. Each sprint has its own folder with a detailed README, links to live project artifacts (Google Sheets, Jira), and relevant code files.

> â ï¸ **Note:** All testing was conducted in the TripleTen sandbox environment. This does not represent work in a production environment or at a real company.

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

Defects logged in Jira: **40** (3 Critical Â· 24 High Â· 9 Medium Â· 4 Low)
Cross-browser issues found: **15+** (Chrome Â· Firefox Â· Edge)

---

## Sprint Index

| Sprint | Topic | Project | Artifact | Status |
|---|---|---|---|---|
| [Sprint 1](sprint-1) | Testing Fundamentals | Manual testing & bug reporting â Urban Routes map UI | [ð Jira Board ESP1](https://rainsol.atlassian.net/jira/software/projects/ESP1/boards/1) | â Accepted |
| [Sprint 2](sprint-2) | Test Design & Documentation | Address field test design (EC/BV, test cases) | [ð Google Sheets](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit) | â Accepted |
| [Sprint 3](sprint-3) | Testing Web Applications | Payment card validation (EC/BV, test cases) | [ð Google Sheets](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit) Â· [ð Jira ESP3](https://rainsol.atlassian.net/jira/software/projects/ESP3/boards/1) | â Accepted |
| [Sprint 4](sprint-4) | APIs | REST API testing â Kits & Fast Delivery endpoints | [ð Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit) Â· [ð¬ Postman](postman/urban_routes_api_collection.json) | â Accepted |
| [Sprint 5](sprint-5) | Understanding Databases | SQL â data integrity queries | [ðï¸ SQL file](sql/urban_routes_data_integrity.sql) | â Complete |
| [Sprint 6](sprint-6) | Testing Mobile Applications | Mobile checklist â Urban Lunch Android app | [ð Google Sheets](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit) | â Accepted |
| Sprint 7 | Python | *(in progress)* | â | ð In Progress |
| Sprint 8 | Browser Automation | Selenium WebDriver â 9 E2E tests scripted (full order flow) | [ð¤ Selenium](selenium/test_urban_routes.py) | â Complete (9 E2E tests scripted and committed to repo) |
| Sprint 9 | Final Project | Applied Testing â capstone | â | â³ Upcoming |

---

## Repository Structure

```
TripleTen-QA-projects-ES/
âââ sprint-1/             â Manual testing & Jira bug reports
âââ sprint-2/             â Test design: address fields (Google Sheets)
âââ sprint-3/             â Test design: card validation (Google Sheets)
âââ sprint-4/             â API testing: kits & fast delivery (Sheets + Postman)
âââ sprint-5/             â SQL: data integrity queries
âââ sprint-6/             â Mobile testing checklist (Google Sheets)
âââ postman/
â   âââ urban_routes_api_collection.json
âââ selenium/
â   âââ test_urban_routes.py  â 9 E2E tests (route, booking, payment, extras)
âââ sql/
â   âââ urban_routes_data_integrity.sql
âââ test-cases/
    âââ urban_routes_test_cases.md
```

---

## Tech Stack

| Area | Tools |
|---|---|
| Manual Testing | Jira (ESP1, ESP3), test case templates, exploratory testing |
| Test Design | Equivalence classes, boundary value analysis, Google Sheets |
| API Testing | Postman (REST: GET/POST, status codes, response schema) |
| Database | PostgreSQL / SQL (JOINs, aggregates, CASE WHEN, subqueries) |
| Mobile Testing | Android Studio Emulator, Android app testing |
| Cross-Browser Testing | Chrome Â· Firefox Â· Edge (15+ issues documented) |
| UI Automation | Python, Pytest, Selenium WebDriver 4, ChromeDriver, Page Object Model |
| Defect Tracking | Jira (projects ESP1, ESP3) |

---

## Defect Summary (All Sprints)

| Category | Total | Critical | High | Medium | Low |
|---|---|---|---|---|---|
| Map & Address UI (S1) | 10 | 0 | 1 | 5 | 4 |
| Card Validation (S3) | 10 | 1 | 8 | 1 | 0 |
| API â Kits (S4) | 11 | 0 | 10 | 1 | 0 |
| API â Fast Delivery (S4) | 3 | 1 | 2 | 0 | 0 |
| Mobile â Urban Lunch (S6) | 6 | 1 | 3 | 2 | 0 |
| **Total** | **40** | **3** | **24** | **9** | **4** |

---

*Each sprint folder contains a full project README with tools used, what was tested, key findings, and links to all artifacts.*
