# selenium — Sprint 8: Urban Routes Browser Automation

Selenium WebDriver test suite automating the full Comfort tariff order flow on
the Urban Routes web application (TripleTen sandbox environment).

**Sprint:** 8 — Browser Automation (TripleTen QA Engineering)
**Status:** ✅ Complete | **Tests:** 14 | **Environment:** TripleTen sandbox

---

## What it tests

End-to-end order flow for the Comfort tariff — from address entry to car search launch:

| Step | Action | Test Coverage |
|------|--------|---------------|
| 1 | Set pickup address ("East 2nd Street, 601") | `smoke` |
| 2 | Set dropoff address ("1300 1st St") | `smoke` |
| 3 | Select Comfort tariff | `smoke` |
| 4 | Open phone number modal | `full` |
| 5 | Enter and confirm phone number | `full` |
| 6 | Open payment method modal | `full` |
| 7 | Enter credit card number | `full` |
| 8 | Enter CVV and confirm card | `full` |
| 9 | Apply promo code | `full` |
| 10 | Toggle blanket/scarves requirement | `full` |
| 11 | Add 2 ice cream to order | `full` |
| 12 | Submit order and verify car search launches | `smoke` · `full` |
| — | Missing required field: phone number | `negative` |
| — | Invalid card number format | `negative` |

---

## Architecture

| Layer | File | Role |
|-------|------|------|
| Tests | `test_urban_routes.py` | Pytest test functions — calls Page Object methods only; zero raw Selenium |
| Page Object | `pages/urban_routes_page.py` | All locators and interactions encapsulated in one class |
| Fixtures | `conftest.py` | Browser setup/teardown, screenshot-on-failure hook |

**No raw Selenium in the test file.** Every selector lives in `urban_routes_page.py`.
If the app's markup changes, one file needs updating — not every test.

---

## Key technical decisions

**Explicit waits throughout**
Every interaction uses `WebDriverWait` with `expected_conditions`. No `time.sleep()` anywhere in the suite. This prevents false failures from network latency and ensures tests fail fast when the app genuinely breaks.

**Screenshot-on-failure hook**
`conftest.py` registers a pytest hook that captures a screenshot at the moment of failure and saves it to `screenshots/`. Failure analysis doesn't require re-running the test.

**Test markers for selective execution**
`smoke` tests cover the critical path only (~2 min) and are intended for CI gates. `full` tests run the complete happy path. `negative` tests validate error conditions. Running `pytest -m smoke` gives fast feedback without the full 14-test suite.

**Page Object encapsulation**
Locators are separated into a `Locators` class within `urban_routes_page.py`. Methods are named after user intent (`select_comfort_tariff()`, `add_ice_cream(n)`) rather than implementation detail (`click_element_by_id()`). Tests read like specifications.

---

## Test markers

```
@pytest.mark.smoke    — critical path, run on every push (~2 min)
@pytest.mark.full     — complete happy path regression
@pytest.mark.negative — error conditions and edge cases
```

---

## Running

```bash
# Install dependencies (from repo root)
pip install -r requirements.txt

# Full suite
pytest selenium/ -v

# Smoke only (fastest feedback)
pytest selenium/ -m smoke

# Negative / edge cases
pytest selenium/ -m negative

# With HTML report
pytest selenium/ --html=reports/test_report.html --self-contained-html
```

> **Environment note:** These tests target the TripleTen sandbox. You must have a valid `APP_URL`
> set in your environment or `.env` file. See `.env.example` in the repo root.

---

## Locators (verified Sprint 8)

| Element | Selector Strategy | Notes |
|---------|-------------------|-------|
| From address field | CSS — `#from` | Direct input |
| To address field | CSS — `#to` | Direct input |
| Comfort tariff | CSS — `.tariff-cards .comfort` | Clicks card to select |
| Phone modal trigger | CSS — `.phone-number-button` | Opens modal overlay |
| Phone input | CSS — `input[type="tel"]` | Inside modal |
| Credit card input | CSS — `input.card-number` | Numeric, 12-digit |
| CVV input | CSS — `input.card-cvv` | 2-digit |
| Promo code input | CSS — `input.promo-code` | Optional text field |
| Blanket toggle | CSS — `.blanket-switch input` | Checkbox toggle |
| Ice cream counter | CSS — `.ice-cream .counter-plus` | Repeated click |
| Order button | CSS — `.smart-button` | Submits order |
| Car search modal | CSS — `.order-header-title` | Confirms search started |

---

## What the test output looks like

```
collected 14 items

selenium/test_urban_routes.py::test_set_route PASSED              [ smoke ]
selenium/test_urban_routes.py::test_select_comfort_tariff PASSED  [ smoke ]
selenium/test_urban_routes.py::test_fill_phone_number PASSED      [ full  ]
selenium/test_urban_routes.py::test_add_credit_card PASSED        [ full  ]
selenium/test_urban_routes.py::test_apply_promo_code PASSED       [ full  ]
selenium/test_urban_routes.py::test_toggle_blanket PASSED         [ full  ]
selenium/test_urban_routes.py::test_add_ice_cream PASSED          [ full  ]
selenium/test_urban_routes.py::test_order_car_search_launches PASSED [ smoke ]
...

14 passed in ~4m 30s
```
