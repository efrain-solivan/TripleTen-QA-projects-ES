# QA Engineering Portfolio — Efrain Solivan

**Program:** TripleTen QA Engineering Apprenticeship
**Author:** Efrain Solivan | [LinkedIn](https://www.linkedin.com/in/efrain-solivan) | [GitHub](https://github.com/efrain-solivan)
**Stack:** Python · Selenium · Pytest · Postman · SQL · Jira · Android Studio
**Progress:** Sprints 1–8 complete · Capstone upcoming (May 2026)

---

## 🌟 Featured: Production UI Automation

**Project:** Live E-Commerce Search & Sort Validation — [Jomashop.com](https://www.jomashop.com)
**Folder:** [`ecommerce_automation/`](./ecommerce_automation/)

Unlike the sandbox sprint projects below, this framework was built against a real production site with active bot detection and a live SPA DOM.

| What | How |
|------|-----|
| **Language & Framework** | Python 3.14 · Pytest · Selenium 4 |
| **Bot detection bypass** | `undetected-chromedriver` defeats PerimeterX (active on Jomashop) |
| **Architecture** | Page Object Model · explicit `WebDriverWait` · zero `time.sleep()` |
| **Stale DOM fix** | JavaScript atomic extraction eliminates `StaleElementReferenceException` on SPA re-renders |
| **Sort validation** | 8-product sample · `min < max` guard prevents vacuous pass on uniform prices |
| **Result** | `$5.99 ≤ $5.99 ≤ $5.99 ≤ $6.99 ≤ $6.99 ≤ $6.99 ≤ $6.99 ≤ $6.99` ✓ |

```
3 passed in 31.23s
```

---

## Sprint Index

| Sprint | Topic | Project | Artifact | Status |
|--------|-------|---------|----------|--------|
| Sprint 1 | Testing Fundamentals | Manual testing & bug reporting — Urban Routes map UI | 📋 Jira Board ESP1 | ✅ Accepted |
| Sprint 2 | Test Design & Documentation | Address field test design (EC/BV, test cases) | 📊 Google Sheets | ✅ Accepted |
| Sprint 3 | Testing Web Applications | Payment card validation (EC/BV, test cases) | 📊 Google Sheets | ✅ Accepted |
| Sprint 4 | APIs | REST API testing — Kits & Fast Delivery endpoints | 📊 Google Sheets · 📬 Postman | ✅ Accepted |
| Sprint 5 | Understanding Databases | SQL — Urban Routes data integrity validation | 🗄️ [SQL file](sql/urban_routes_data_integrity.sql) | ✅ Complete |
| Sprint 6 | Testing Mobile Applications | Mobile checklist — Urban Lunch Android app | 📊 Google Sheets | ✅ Accepted |
| Sprint 7 | Python | Python scripting for QA automation | — | ✅ Complete |
| Sprint 8 | Browser Automation | Selenium WebDriver — Urban Routes full order flow | 🤖 [selenium/](selenium/) | ✅ Complete |
| Sprint 9 | Final Project | Applied Testing — capstone | — | ⏳ Upcoming |

> ⚠️ Sprints 1–8 were completed in the TripleTen sandbox environment against a test application. The `ecommerce_automation/` project above targets a live production site.

---

## Repository Structure

```text
TripleTen-QA-projects-ES/
│
├── ecommerce_automation/        ← 🌟 Live Production Framework (Jomashop)
│   ├── conftest.py              ← undetected_chromedriver session fixture
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── pages/
│   │   └── search_page.py      ← Page Object Model
│   ├── tests/
│   │   └── test_search_filter.py
│   └── utils/
│       └── wait_helpers.py     ← explicit WebDriverWait utilities
│
├── selenium/                    ← Sprint 8 — Urban Routes order flow
│   ├── conftest.py
│   ├── pages/
│   │   └── urban_routes_page.py
│   └── test_urban_routes.py
│
├── postman/
│   └── urban_routes_api_collection.json
│
├── sql/
│   └── urban_routes_data_integrity.sql
│
├── test-cases/
│   └── urban_routes_test_cases.md
│
├── sprint-1/  through  sprint-6/   ← per-sprint READMEs with reviewer feedback
│
└── README.md
```
