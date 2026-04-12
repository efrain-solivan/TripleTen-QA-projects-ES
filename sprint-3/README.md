# Sprint 3 — Testing Web Applications

## Project 3: Urban Routes — Payment Card Validation

**Program:** TripleTen QA Engineering Apprenticeship  
**Sprint:** 3 — Testing Web Applications  
**Duration:** 8 hr  
**Status:** ✅ Accepted (3 iterations)  
**Reviewer feedback:** *"Well done on completing your project! 👍 Your progress is something to be proud of."*

---

## 📊 Google Sheets Project

**[Open Project 3 in Google Sheets →](https://docs.google.com/spreadsheets/d/1tyb3C0jYfA0jdLqO3gJ0puDvY3OEUNAXka8Hxg9wG5U/edit)**

---

## What I Tested

Designed a full test suite for the **payment card entry form** in Urban Routes, covering the card number field (FR-CS32) and CVV/CVC field (FR-CS33) using formal test design techniques.

**Requirement FR-CS32:** User must enter card info and click "Add" to order a car  
**Requirement FR-CS33:** CVV/CVC field validation

---

## Tools & Techniques Used

| Tool / Technique | Purpose |
|---|---|
| Requirements Analysis | Decomposed card payment requirements into atomic steps |
| Equivalence Class (EC) partitioning | Valid/invalid card number and CVV classes |
| Boundary Value Analysis (BVA) | Length boundaries for card number (11, 12, 13 digits) and CVV (1, 2, 3 digits) |
| Google Sheets | Structured all test design artifacts |

---

## Spreadsheet Structure

| Tab | Contents |
|---|---|
| 1. Requirements Analysis | Requirement decomposition for FR-CS32 and FR-CS33 |
| 3.1. EC and BV | Equivalence classes and boundary values for Card Number and CVV/CVC |
| 3.2. Test Cases | Full test cases with steps and expected results |
| Report | Execution summary with pass/fail counts |

---

## Equivalence Classes Covered (Card Number)

| Class | Example | Expected |
|---|---|---|
| Empty input | (none) | Reject |
| Less than 12 digits (BV: 11) | 12345678901 | Reject |
| Exactly 12 digits ✅ (BV: 12) | 1234 5678 9012 | Accept |
| More than 12 digits (BV: 13) | 1234567890123 | Reject |
| Non-numeric characters | 1234 56AB 9012 | Reject |
| Special characters | 1234 56@# 9012 | Reject |
| Input without auto-format on blur | 123456789012 (no spaces) | Reject |
| Boundary block values | 0000 0000 0000, 9999 9999 9999 | Accept/Reject |
| Mixed valid/invalid segments | 1234 9999 000A | Reject |

---

## Bugs Found

Key defects identified during test execution (logged in Jira ESP3):

| ID | Description | Severity |
|---|---|---|
| ESP3-14 | App crashes when the Aero Taxi icon is clicked | Critical |
| ESP3-16 | Card number field accepts fewer than 12 characters | High |
| ESP3-17 | Card number field accepts more than 12 characters | High |
| ESP3-18 | Card number field accepts alphabetical characters | High |
| ESP3-19 | Card number field accepts symbols | High |
| ESP3-20 | Card number field does not auto-format on blur | Medium |
| ESP3-21 | Card number field accepts mixed valid/invalid card segments | High |
| ESP3-22 | CVV/CVC field accepts fewer than 2 digits | High |
| ESP3-23 | CVV/CVC field accepts more than 2 digits | High |

---

## Key Skills Demonstrated

- Applying EC partitioning and BVA to a form input field
- Writing boundary-focused test cases
- Identifying critical payment validation defects
- Documenting test results with severity classification
