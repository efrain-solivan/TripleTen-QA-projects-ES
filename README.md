# Urban Routes — QA Engineering Portfolio

**Program:** TripleTen QA Engineering Apprenticeship  
**Project:** Urban Routes — Ride-Hailing Web Application  
**Author:** Efrain Solivan  
**Test Stack:** SQL · Postman · Selenium WebDriver · Pytest · Jira  

---

## Project Description

Urban Routes is a web-based transportation application that allows users to enter an origin and destination address, select a service type (Optimal, Flash, Personal), choose a payment method, and request a driver. This repository documents quality assurance activities performed across all TripleTen sprint projects in the simulation environment.

> ⚠️ **Note:** All testing was conducted in the TripleTen sandbox. This does not represent work in a production environment or at a real company.

---

## Repository Structure

```
TripleTen-QA-projects-ES/
│
├── README.md                          ← This file
│
├── sql/
│   └── urban_routes_data_integrity.sql   ← JOIN queries for DB validation (Sprint 2)
│
├── postman/
│   └── urban_routes_api_collection.json  ← Exported Postman collection (Sprints 3–4)
│
├── selenium/
│   └── test_urban_routes.py              ← Selenium WebDriver + Pytest scripts (Sprint 5)
│
└── test-cases/
    └── urban_routes_test_cases.md        ← Manual test cases: all sprints
```

---

## Sprint Overview

| Sprint | Focus Area | Tool(s) | File |
|---|---|---|---|
| Sprint 1 | Manual Testing — Map & Address UI | Jira / Markdown | [test-cases/urban_routes_test_cases.md](test-cases/urban_routes_test_cases.md) |
| Sprint 2 | Database Integrity — SQL JOINs | PostgreSQL | [sql/urban_routes_data_integrity.sql](sql/urban_routes_data_integrity.sql) |
| Sprint 3 | API Testing — Kits & Users endpoints | Postman | [postman/urban_routes_api_collection.json](postman/urban_routes_api_collection.json) |
| Sprint 4 | API Testing — Fast Delivery endpoint | Postman | [postman/urban_routes_api_collection.json](postman/urban_routes_api_collection.json) |
| Sprint 5 | UI Automation — Full order flow | Selenium + Pytest | [selenium/test_urban_routes.py](selenium/test_urban_routes.py) |

---

## Test Coverage Areas

| Area | Tool | Description |
|---|---|---|
| Database integrity | SQL (PostgreSQL) | Validates table relationships using JOINs, orphan checks, duplicate detection |
| API testing — Kits | Postman | Verifies POST /kits endpoints: create, add products, invalid inputs |
| API testing — Fast Delivery | Postman | Verifies POST /fast-delivery: eligibility, operating hours, pricing bands |
| UI automation | Selenium + Pytest | Full taxi order flow: route → tariff → phone → card → extras → order |
| Manual test cases | Markdown / Jira | Positive, negative, and boundary test case design for all sprints |

---

## Technologies Used

- **Python 3.10+** with `pytest` and `selenium`
- **ChromeDriver** (matched to installed browser version)
- **Postman** v10+
- **PostgreSQL** (TripleTen sandbox environment)
- **Jira** for defect tracking and sprint management

---

## How to Run the Selenium Tests

```bash
# 1. Install dependencies
pip install pytest selenium

# 2. Confirm ChromeDriver is on your PATH

# 3. Run all tests
pytest selenium/test_urban_routes.py -v

# 4. Run a single test
pytest selenium/test_urban_routes.py::TestOrderFlow::test_set_route -v
```

---

## Defects Found — Jira Project ESP3

### Sprint 1 — Map & Address Behavior

| ID | Description | Severity | Status |
|---|---|---|---|
| ESP3-1 | Selecting the "From" field auto-populates an address without user input | Medium | To Do |
| ESP3-2 | Typing "Subway" in the "To" field does not show the subway station list | High | To Do |
| ESP3-3 | Clicking the "From" field populates a random address | Medium | To Do |
| ESP3-4 | Map does not zoom to address pin after user inputs an address | Low | To Do |
| ESP3-5 | Hovering near the Map mode button labels the Landscape option as "Terrain" | Low | To Do |
| ESP3-8 | Hovering near the Satellite mode button does not open the Map objects list | Medium | To Do |
| ESP3-9 | Clicking a place on the map does not properly zoom to the address pin | Low | To Do |
| ESP3-11 | Clicking the app logo does not display the app information panel | Low | To Do |
| ESP3-12 | Clicking an area header (e.g. Hollywood) opens the place information display | Medium | To Do |
| ESP3-13 | Clicking the "To" field auto-populates an address without user input | Medium | To Do |

### Sprint 2 — Payment Card Validation

| ID | Description | Severity | Status |
|---|---|---|---|
| ESP3-14 | App crashes when the Aero Taxi icon is clicked | Critical | To Do |
| ESP3-15 | Aero Taxi mode activation cannot be validated | High | To Do |
| ESP3-16 | Card number field accepts fewer than 12 characters | High | To Do |
| ESP3-17 | Card number field accepts more than 12 characters | High | To Do |
| ESP3-18 | Card number field accepts alphabetical characters | High | To Do |
| ESP3-19 | Card number field accepts symbols | High | To Do |
| ESP3-20 | Card number field does not auto-format on blur | Medium | To Do |
| ESP3-21 | Card number field accepts mixed valid/invalid card segments | High | To Do |
| ESP3-22 | CVV/CVC field accepts fewer than 2 digits | High | To Do |
| ESP3-23 | CVV/CVC field accepts more than 2 digits | High | To Do |

### Sprint 3 — API: Kits Endpoint

| ID | Description | Severity | Status |
|---|---|---|---|
| ESP3-25 | POST /kits/2/products — quantity 0 returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-26 | POST /kits/10/products — negative quantity returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-27 | POST /kits/10/products — non-existent product ID returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-28 | POST /kits/10/products — empty productsList returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-29 | POST /kits/2/products — missing ID field returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-30 | POST /kits/3/products — missing quantity field returns 500 instead of 400 | High | To Do |
| ESP3-31 | POST /kits/3/products — string ID returns 500 Internal Server Error instead of 400 | High | To Do |
| ESP3-32 | POST /kits/10/products — quantity null returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-36 | POST /kits/7/products — empty body {} returns 200 OK instead of 400 Bad Request | High | To Do |
| ESP3-37 | POST /kits/7/products — nested productsList returns 500 instead of 400 Bad Request | High | To Do |
| ESP3-38 | POST /kits/-1/products — null product returns 404 Not Found instead of 400 Bad Request | Medium | To Do |

### Sprint 4 — API: Fast Delivery & UI Bugs

| ID | Description | Severity | Status |
|---|---|---|---|
| ESP3-39 | POST /fast-delivery — invalid XML payload returns 500 instead of 400 | High | To Do |
| ESP3-40 | POST /fast-delivery — isItPossibleToDeliver: true returned outside operating hours | Critical | To Do |
| ESP3-41 | POST /fast-delivery — delivery cost stays at 6 instead of 7 when weight/count exceeds Band 6 | High | To Do |
| ESP3-42 | Order Confirmation screen total excludes delivery cost | Critical | To Do |
| ESP3-43 | Delivery notification text is incorrectly sized and missing the temperature warning | Medium | To Do |
| ESP3-44 | Map pins do not display numerical order for pick-up points | Medium | To Do |
| ESP3-45 | Long restaurant names overlap surrounding text on the Dish Details screen | Low | To Do |
| ESP3-46 | Order tracking screen omits remaining cooking time entirely | High | To Do |
| ESP3-47 | Delivered screen map displays incorrect pick-up location pin | High | To Do |

---

## Defect Summary

| Total | Critical | High | Medium | Low |
|---|---|---|---|---|
| 30 | 3 | 19 | 6 | 4 |

---

## Author Notes

Selenium scripts use a lite Page Object Model (POM) pattern to separate locators from test logic. Test cases follow the TripleTen standard template: ID, title, preconditions, steps, expected result, actual result, status. All defects were logged in Jira under project ESP3 and are tracked in the backlog above.
