import re
from typing import List

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.wait_helpers import (
    wait_for_element_clickable,
    wait_for_elements,
    wait_for_url_contains,
)


class SearchPage:
    # Locators — verified live against jomashop.com on 2026-04-14
    SEARCH_INPUT   = (By.CSS_SELECTOR, "input.search-field-input")
    SORT_BUTTON    = (By.CSS_SELECTOR, "button.btn-sort")
    SORT_PRICE_ASC = (By.CSS_SELECTOR, "a.price_asc")
    PRICE_ELEMENTS = (By.CSS_SELECTOR, "div.now-price")
    SORT_URL_FRAGMENT = "price_default_asc"

    POPUP_SELECTORS = [
        (By.CSS_SELECTOR, "button.modal-close"),
        (By.CSS_SELECTOR, "button[aria-label='Close']"),
        (By.CSS_SELECTOR, ".bottom-promo .close"),
    ]

    def __init__(self, driver: WebDriver, base_url: str):
        self._driver = driver
        self._base_url = base_url

    def navigate_to_home(self):
        self._driver.get(self._base_url)
        return self

    def dismiss_popups(self, timeout=4):
        for by, locator in self.POPUP_SELECTORS:
            try:
                btn = wait_for_element_clickable(self._driver, by, locator, timeout=timeout)
                btn.click()
            except (TimeoutException, NoSuchElementException):
                pass
        return self

    def search_for(self, query: str):
        # Jomashop's search input uses React synthetic events that do not fire
        # correctly under headless Chrome — .send_keys(Keys.RETURN) and
        # ActionChains both fail to trigger the navigation event handler.
        # Direct URL navigation is the correct automation approach here:
        # it puts the browser in the exact same state a successful search would,
        # making it the reliable setup step for testing sort/filter logic.
        from urllib.parse import quote_plus
        self._driver.get(f"{self._base_url}/search?q={quote_plus(query)}")
        return self

    def wait_for_results(self, min_products=3):
        # Guard: confirm we actually landed on the search results page.
        # Without this, the test silently passes on the homepage because
        # div.now-price exists there too (watches, accessories, etc.).
        wait_for_url_contains(self._driver, "/search")
        wait_for_elements(self._driver, *self.PRICE_ELEMENTS, min_count=min_products)
        return self

    def sort_by_price_low_to_high(self):
        sort_btn = wait_for_element_clickable(self._driver, *self.SORT_BUTTON)
        sort_btn.click()
        price_asc = wait_for_element_clickable(self._driver, *self.SORT_PRICE_ASC)
        price_asc.click()
        wait_for_url_contains(self._driver, self.SORT_URL_FRAGMENT)
        wait_for_elements(self._driver, *self.PRICE_ELEMENTS, min_count=3)
        return self

    def get_first_n_prices(self, n=3) -> List[float]:
        # Scroll to trigger lazy-loading of the second product row.
        self._driver.execute_script("window.scrollBy(0, 600);")

        # Confirm at least n price elements exist in the DOM before reading.
        wait_for_elements(self._driver, *self.PRICE_ELEMENTS, min_count=n)

        # WHY JavaScript instead of iterating WebElement references?
        # After a scroll, Jomashop's SPA may re-render product cards. Any
        # WebElement reference captured before the re-render becomes stale,
        # raising StaleElementReferenceException on .text access.
        # JavaScript executes atomically against one DOM snapshot — no stale
        # references are possible because there is no gap between capture and read.
        raw_texts: list = self._driver.execute_script(
            "return Array.from(document.querySelectorAll('div.now-price'))"
            ".slice(0, arguments[0]).map(el => el.textContent.trim());",
            n,
        )

        prices = []
        for raw in raw_texts:
            cleaned = re.sub(r"[^\d.]", "", raw)
            if not cleaned:
                raise ValueError(f"Cannot parse price from: '{raw}'")
            prices.append(float(cleaned))
        return prices

    @staticmethod
    def assert_prices_sorted_ascending(prices: List[float]):
        for i in range(len(prices) - 1):
            assert prices[i] <= prices[i + 1], (
                f"Sort violation at index {i}: "
                f"${prices[i]:.2f} > ${prices[i+1]:.2f}\n"
                f"Full sequence: {[f'${p:.2f}' for p in prices]}"
            )
