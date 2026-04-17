# ecommerce_automation

Selenium UI test framework validating search and price-sort logic on
[Jomashop.com](https://www.jomashop.com) — a live production e-commerce site
targeting production environments with dynamic bot-mitigation systems.

## What it tests

> Search "Arabic fragrances" → sort by Price: Low to High → assert the first 8
> rendered products are in non-decreasing price order.

## Tech decisions worth noting

**CDP fingerprint modification for stable production test execution**
Standard Selenium WebDriver exposes an automatable browser signature that triggers bot-mitigation overlays on live production sites. The framework applies CDP-level fingerprint modification via `undetected-chromedriver` to present a browser profile consistent with organic user traffic, enabling stable, repeatable test runs without disrupting the site's protective systems.

**JavaScript price extraction instead of WebElement iteration**
After a sort click, Jomashop's Algolia-powered SPA re-renders the product grid.
Any `WebElement` reference captured before the re-render raises
`StaleElementReferenceException` on `.text` access. Extracting prices in a
single `driver.execute_script()` call runs atomically against one DOM snapshot —
stale references are structurally impossible.

**`min < max` guard on the sort assertion**
The cheapest Arabic fragrances on Jomashop cluster at the same price point
(e.g. `$19.99 × 3`). Three identical prices satisfy `price[0] <= price[1] <=
price[2]` vacuously — a broken sort would still pass. Sampling 8 products and
asserting `min(prices) < max(prices)` ensures the sample contains genuine
variation before the sort order check runs.

## Structure

```
ecommerce_automation/
├── conftest.py               # Session-scoped undetected_chromedriver fixture
├── pytest.ini                # Discovery, markers, warning filters
├── requirements.txt
├── pages/
│   └── search_page.py        # Page Object Model — all locators in one place
├── tests/
│   └── test_search_filter.py # 3 tests: smoke → URL assert → sort order
└── utils/
    └── wait_helpers.py       # Explicit WebDriverWait — no time.sleep()
```

## Running

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
pytest tests/                  # visible Chrome (default)
pytest tests/ --headless=true  # headless
pytest tests/ -m smoke         # smoke only
```

## Test results

Verified passing on Python 3.14.2 / pytest-9.0.3 / Windows (2026-04-16):

```
========================= test session starts =========================
platform win32 -- Python 3.14.2, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\rains\Downloads\ecommerce_automation
configfile: pytest.ini
collected 3 items

tests/test_search_filter.py::test_search_returns_results
  [PASS] Search loaded. First 3 prices: [19.99, 19.99, 19.99]
PASSED
tests/test_search_filter.py::test_sort_label_updates_to_price_low_to_high
  [PASS] Sort applied. URL: https://www.jomashop.com/search?q=Arabic%20fragrances&sortBy=productionM2_default_products_price_default_asc
PASSED
tests/test_search_filter.py::test_price_sort_order_ascending[8]
  Prices after sort (8 products): [5.99, 5.99, 5.99, 6.99, 6.99, 6.99, 6.99, 6.99]
  [PASS] $5.99 <= $5.99 <= $5.99 <= $6.99 <= $6.99 <= $6.99 <= $6.99 <= $6.99
PASSED

========================= 3 passed in 31.23s ==========================
```

## Locators (verified 2026-04-14)

| Element | Selector | Notes |
|---------|----------|-------|
| Search input | `input.search-field-input` | React-controlled — navigated via URL |
| Sort button | `button.btn-sort` | Custom Bootstrap dropdown trigger |
| Price Low→High | `a.price_asc` | Algolia sort option |
| Product prices | `div.now-price` | Current/sale price per card |
