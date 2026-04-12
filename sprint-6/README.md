# Sprint 6 — Testing Mobile Applications

## Project 6: Urban Lunch Mobile App — Test Checklist

**Program:** TripleTen QA Engineering Apprenticeship  
**Sprint:** 6 — Testing Mobile Applications  
**Duration:** 8 hr 40 min  
**Status:** ✅ Accepted (2 iterations)  
**Achievement:** 🏅 Get Your Mobile Tester Badge  
**Reviewer feedback:** *"Another project down—amazing work! 🎉 You've taken a big step by diving into mobile testing, using an emulator, and systematically testing the app's key flows."*

---

## 📊 Google Sheets Project

**[Open Project 6 in Google Sheets →](https://docs.google.com/spreadsheets/d/16vPGkMI4pK5eJek2JdMuR2a2MiH25km0KZPszijaxUA/edit)**

---

## What I Tested

Executed a **full end-to-end mobile testing checklist** for the **Urban Lunch** food delivery mobile application using an Android emulator. The checklist covered the complete user journey from opening the app through order delivery.

**App under test:** Urban Lunch — food delivery mobile app (Android)

---

## Tools Used

| Tool | Purpose |
|---|---|
| Android Studio Emulator | Running the Urban Lunch app on a virtual device |
| Google Sheets | Structured checklist with PASSED/FAILED results per test case |
| Jira (ESP3) | Logging bugs found during mobile testing |

---

## Test Coverage (by Screen Flow)

| Section | # Tests | Key Checks |
|---|---|---|
| 1. Selecting a pick-up location | 13 | Geolocation permission, map markers, tap selection, footer progress |
| 2. Choice of dishes | ~8 | Dish list display, item names/prices, quantity controls, restaurant names |
| 3. Placing an order | ~8 | Order summary, delivery cost display, confirmation screen |
| 4. Order tracking / Order pick-up | 10 | Map routes, cost display, cooking time, scrollable item list |
| 5. The order is delivered | 6 | Auto-navigation to delivered screen, pick-up point map pin, notification text |

---

## Notable Failures Found

| ID | Description | Severity |
|---|---|---|
| 1.02 | Map does not show pick-up points with numbered markers | Medium |
| 4.05 | Routes do not show remaining cooking time | High |
| 5.02 | Delivered screen map shows incorrect pick-up location pin | High |
| 5.03 | Notification text is incorrectly sized and missing temperature warning | Medium |
| ESP3-42 | Order Confirmation screen total excludes delivery cost | Critical |
| ESP3-43 | Delivery notification text is incorrectly sized and missing the temperature warning | Medium |
| ESP3-44 | Map pins do not display numerical order for pick-up points | Medium |
| ESP3-46 | Order tracking screen omits remaining cooking time entirely | High |
| ESP3-47 | Delivered screen map displays incorrect pick-up location pin | High |

---

## Key Skills Demonstrated

- Setting up and using an Android emulator (Android Studio)
- Executing a structured mobile test checklist against real app behavior
- Identifying and documenting UI and functional defects on a mobile platform
- Testing across full end-to-end user flows (onboarding → order → delivery)
- Recording PASSED/FAILED results and bug IDs in a shareable format
