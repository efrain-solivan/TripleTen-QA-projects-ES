# Sprint 4 — APIs

## Project 4: Urban Routes — API Testing (Kits & Fast Delivery)

**Program:** TripleTen QA Engineering Apprenticeship  
**Sprint:** 4 — APIs  
**Duration:** 12 hr  
**Status:** ✅ Accepted (7 iterations)  
**Achievement:** 🏅 Becoming an API Tester  
**Reviewer feedback:** *"Congratulations on reaching an important milestone and completing Sprint 4! You've made real progress mastering API testing."*

---

## 📊 Google Sheets Project

**[Open Project 4 in Google Sheets →](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit)**

---

## 📬 Postman Collection

See [`../postman/urban_routes_api_collection.json`](../postman/urban_routes_api_collection.json) for the full exported Postman collection with automated test scripts.

---

## What I Tested

Designed and executed API tests for the **Urban Routes backend REST API**, focusing on two requirements:

**Requirement 1:** Working with Kits — `POST /api/v1/kits/{id}/products`  
**Requirement 2:** Fast Delivery — `POST /fast-delivery/v3.1.1/calculate-delivery`

---

## Tools Used

| Tool | Purpose |
|---|---|
| Postman | Sending HTTP requests, writing test scripts, checking response codes and schemas |
| Google Sheets | Documenting test cases, test data, and expected vs actual responses |
| Jira (ESP3) | Logging API defects |

---

## Test Cases — Kits Endpoint

| # | Test Case | Expected |
|---|---|---|
| 1 | Valid product add succeeds | 200 OK |
| 2 | Quantity = 1 (lower boundary) | 200 OK |
| 3 | Negative quantity rejected | 400 Bad Request |
| 4 | Non-existent product ID rejected | 400 Bad Request |
| 5 | Quantity = 0 rejected | 400 Bad Request |
| 6 | Malformed body rejected | 400 Bad Request |
| 7 | Empty productsList rejected | 400 Bad Request |

---

## Bugs Found (API — Kits)

| ID | Description | Severity |
|---|---|---|
| ESP3-25 | quantity 0 returns 200 OK instead of 400 | High |
| ESP3-26 | negative quantity returns 200 OK instead of 400 | High |
| ESP3-27 | non-existent product ID returns 200 OK instead of 400 | High |
| ESP3-28 | empty productsList returns 200 OK instead of 400 | High |
| ESP3-29 | missing ID field returns 200 OK instead of 400 | High |
| ESP3-30 | missing quantity field returns 500 instead of 400 | High |
| ESP3-31 | string ID returns 500 instead of 400 | High |
| ESP3-32 | null quantity returns 200 OK instead of 400 | High |
| ESP3-36 | empty body {} returns 200 OK instead of 400 | High |
| ESP3-37 | nested productsList returns 500 instead of 400 | High |
| ESP3-38 | null product on kit -1 returns 404 instead of 400 | Medium |

## Bugs Found (API — Fast Delivery)

| ID | Description | Severity |
|---|---|---|
| ESP3-39 | Invalid XML payload returns 500 instead of 400 | High |
| ESP3-40 | isItPossibleToDeliver: true returned outside operating hours | Critical |
| ESP3-41 | Delivery cost stays at 6 instead of 7 when weight/count exceeds Band 6 | High |

---

## Key Skills Demonstrated

- REST API testing using Postman (GET, POST, status code validation, response body validation)
- Designing test cases specifically for API endpoints (positive, negative, boundary)
- Identifying server-side validation failures (500s that should be 400s)
- Documenting API defects with endpoint, request body, expected vs actual response
