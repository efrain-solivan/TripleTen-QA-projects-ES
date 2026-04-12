# Sprint 1 — Testing Fundamentals

## Project 1: Urban Routes Manual Testing & Bug Reporting

**Program:** TripleTen QA Engineering Apprenticeship  
**Sprint:** 1 — Testing Fundamentals  
**Duration:** 5 hr  
**Status:** ✅ Accepted (2 iterations)  
**Reviewer feedback:** *"Your task looks great! Congratulations on your accomplishment! Following test cases and reporting bugs are fundamental aspects of the QA profession."*

---

## What I Tested

Urban Routes is a ride-hailing web application. In this sprint I performed **exploratory and scripted manual testing** on the map and address input features using the Urban Routes sandbox environment.

**App under test:** Urban Routes — map interface, "From" / "To" address fields, mode selection, and UI elements.

---

## Tools Used

| Tool | Purpose |
|---|---|
| Urban Routes sandbox | Live application under test |
| Jira (project ESP1) | Bug tracking and reporting |
| Test case template | Structured test execution |

---

## Deliverable

📋 **Jira Project Board:** [ESP1 — Urban Routes Sprint 1](https://rainsol.atlassian.net/jira/software/projects/ESP1/boards/1)

The board contains all test cases executed and all bugs reported during this sprint.

---

## Bugs Found (Sprint 1)

| ID | Description | Severity |
|---|---|---|
| ESP3-1 | Selecting the "From" field auto-populates an address without user input | Medium |
| ESP3-2 | Typing "Subway" in the "To" field does not show the subway station list | High |
| ESP3-3 | Clicking the "From" field populates a random address | Medium |
| ESP3-4 | Map does not zoom to address pin after user inputs an address | Low |
| ESP3-5 | Hovering near the Map mode button labels the Landscape option as "Terrain" | Low |
| ESP3-8 | Hovering near the Satellite mode button does not open the Map objects list | Medium |
| ESP3-9 | Clicking a place on the map does not properly zoom to the address pin | Low |
| ESP3-11 | Clicking the app logo does not display the app information panel | Low |
| ESP3-12 | Clicking an area header (e.g. Hollywood) opens the place information display | Medium |
| ESP3-13 | Clicking the "To" field auto-populates an address without user input | Medium |

**Total: 10 bugs** (1 High · 5 Medium · 4 Low)

---

## Key Skills Demonstrated

- Exploratory testing of a web application
- Writing structured bug reports (Summary, Environment, Preconditions, Steps, Expected vs Actual Result)
- Tracking defects in Jira with proper severity classification
- Reading and applying test cases in a real-world-style project simulation
