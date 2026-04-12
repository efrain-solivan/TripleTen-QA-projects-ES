# Sprint 2 — Test Design and Documentation

## Project 2: Urban Routes — Address Field Test Design

**Program:** TripleTen QA Engineering Apprenticeship  
**Sprint:** 2 — Test Design and Documentation  
**Duration:** 7 hr 5 min  
**Status:** ✅ Accepted (2 iterations)  
**Reviewer feedback:** *"Efrain, congratulations, you passed the assignment! Solid work on completing your project! Keep going!"*

---

## 📊 Google Sheets Project

**[Open Project 2 in Google Sheets →](https://docs.google.com/spreadsheets/d/180Ii-U0EN1SYws9RIyir1VxOzOrXp7QoLWwHGU9pvdU/edit)**

---

## What I Tested

Designed a full test suite for the **"From" and "To" address input fields** of the Urban Routes web application, applying formal test design techniques.

---

## Tools & Techniques Used

| Tool / Technique | Purpose |
|---|---|
| Requirements Analysis | Decomposed functional requirements into atomic, testable conditions |
| Test Planning | Mapped each requirement to the test plan section where it is specified |
| Equivalence Class (EC) partitioning | Grouped valid/invalid inputs into classes to minimize test cases |
| Boundary Value Analysis (BVA) | Identified boundary values (0, 1, 49, 50, 51 chars) for length limits |
| Google Sheets | Structured all artifacts in a shared, reviewable format |

---

## Spreadsheet Structure

| Tab | Contents |
|---|---|
| 1. Requirements Analysis | Atomic block decomposition of FR-1 (From field) and FR-2 (To field) requirements |
| 2. Test Planning | Table mapping each test plan section to its source location |
| 3.1. EC and BV | Equivalence classes and boundary values for From/To fields |
| 3.2. Test Cases | Full test cases: ID, description, precondition, steps, test technique |
| Report | Summary: 22 test cases, 0 Pass (0%), 22 Fail (100%) |

---

## Key Findings

- **22 test cases** written and executed
- **22 failures** — all tests failed, confirming widespread input validation defects in the app
- Fields accept invalid characters, don't enforce length limits, and don't properly trim leading/trailing spaces
- These defects were logged in Jira under project ESP3

---

## Key Skills Demonstrated

- Requirements decomposition into atomic verifiable conditions
- Applying equivalence class partitioning and boundary value analysis
- Writing structured test cases (positive, negative, boundary)
- Documenting a test execution report with pass/fail metrics
