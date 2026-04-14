from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 15


def wait_for_element(driver: WebDriver, by: str, locator: str, timeout=DEFAULT_TIMEOUT) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator)),
        message=f"Element not found after {timeout}s: [{by}] '{locator}'",
    )


def wait_for_elements(driver: WebDriver, by: str, locator: str, min_count=1, timeout=DEFAULT_TIMEOUT) -> List[WebElement]:
    def _enough(d):
        els = d.find_elements(by, locator)
        return els if len(els) >= min_count else False

    return WebDriverWait(driver, timeout).until(
        _enough,
        message=f"Expected >= {min_count} elements after {timeout}s: [{by}] '{locator}'",
    )


def wait_for_element_clickable(driver: WebDriver, by: str, locator: str, timeout=DEFAULT_TIMEOUT) -> WebElement:
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator)),
        message=f"Element not clickable after {timeout}s: [{by}] '{locator}'",
    )


def wait_for_url_contains(driver: WebDriver, fragment: str, timeout=DEFAULT_TIMEOUT) -> None:
    WebDriverWait(driver, timeout).until(
        EC.url_contains(fragment),
        message=f"URL did not contain '{fragment}' after {timeout}s",
    )
