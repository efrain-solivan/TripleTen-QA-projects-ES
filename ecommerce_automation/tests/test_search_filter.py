import pytest
from pages.search_page import SearchPage

SEARCH_QUERY = "Arabic fragrances"


@pytest.fixture(scope="module")
def search_page(driver, base_url):
    return SearchPage(driver=driver, base_url=base_url)


@pytest.mark.smoke
def test_search_returns_results(search_page):
    """GIVEN homepage loaded WHEN searching 'Arabic fragrances' THEN 3+ products appear."""
    search_page.navigate_to_home()
    search_page.dismiss_popups()
    search_page.search_for(SEARCH_QUERY)
    search_page.wait_for_results(min_products=3)

    prices = search_page.get_first_n_prices(n=3)

    assert len(prices) == 3
    assert all(p > 0 for p in prices), f"All prices must be positive. Got: {prices}"
    print(f"\n  [PASS] Search loaded. First 3 prices: {prices}")


@pytest.mark.regression
def test_sort_label_updates_to_price_low_to_high(search_page, driver):
    """GIVEN results shown WHEN sort 'Price: Low to High' clicked THEN URL confirms ascending sort."""
    search_page.sort_by_price_low_to_high()

    current_url = driver.current_url
    assert "price_default_asc" in current_url, (
        f"Expected 'price_default_asc' in URL. Got: {current_url}"
    )
    print(f"\n  [PASS] Sort applied. URL: {current_url}")


@pytest.mark.regression
@pytest.mark.parametrize("n_products", [8])
def test_price_sort_order_ascending(search_page, n_products):
    """
    GIVEN sorted by price asc WHEN first 8 prices extracted (2 rows after scroll)
    THEN the sequence is non-decreasing AND contains at least two distinct values.

    WHY n=8?
      Jomashop renders 4 products per row. After one scroll, two full rows are
      in the DOM — 8 products. This is reliable without deep lazy-loading waits,
      and large enough that a broken sort would almost certainly produce a
      violation across 8 real price points.

    WHY pytest.skip on uniform sample?
      If all 8 prices are identical the ascending assertion still passes vacuously
      — it tells us nothing about sort correctness. We skip rather than fail
      because the data limitation is the site's, not a bug in our code.
      The skip message clearly signals what to investigate.
    """
    prices = search_page.get_first_n_prices(n=n_products)
    print(f"\n  Prices after sort ({n_products} products): {prices}")

    # Guard: if every price is identical the sort assertion is vacuously true.
    # Skip with an explicit message rather than letting a meaningless pass through.
    if min(prices) == max(prices):
        pytest.skip(
            f"All {n_products} sampled prices are ${prices[0]:.2f} — uniform sample. "
            f"Sort order cannot be validated. Broaden the search query or increase n."
        )

    SearchPage.assert_prices_sorted_ascending(prices)
    print("  [PASS] " + " <= ".join(f"${p:.2f}" for p in prices))
