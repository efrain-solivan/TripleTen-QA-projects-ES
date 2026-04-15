# selenium — Sprint 8: Urban Routes Browser Automation

Selenium WebDriver test suite automating the full Comfort tariff order flow on
the Urban Routes web application (TripleTen sandbox environment).

## What it tests

End-to-end order flow for the Comfort tariff:
- Set pickup and dropoff addresses
- Select Comfort tariff
- Fill phone number via modal
- Add credit card and apply promo code
- Toggle blanket/scarves requirement
- Add ice cream to order
- Verify car search launches

## Architecture

| Layer | File | Role |
|-------|------|------|
| Tests | `test_urban_routes.py` | Pytest test functions — calls Page Object methods only |
| Page Object | `pages/urban_routes_page.py` | All locators and interactions in one class |
| Fixtures | `conftest.py` | Browser setup, screenshot-on-failure hook |

**No raw Selenium in the test file.** All selectors live in `urban_routes_page.py`.
If the app's markup changes, one file needs updating — not every test.

## Test markers

```
@pytest.mark.smoke    — critical path, run on every push (~2 min)
@pytest.mark.full     — complete happy path regression
@pytest.mark.negative — error conditions and edge cases
```

## Running

```bash
pip install -r requirements.txt
pytest selenium/                    # full suite
pytest selenium/ -m smoke           # smoke only
pytest selenium/ -m negative        # edge cases only
```

## Sprint context

**Sprint:** 8 — Browser Automation (TripleTen QA Engineering)
**Environment:** TripleTen sandbox (not a production app)
**Status:** ✅ Complete
