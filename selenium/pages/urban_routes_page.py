"""
pages/urban_routes_page.py — Page Object Model for Urban Routes web app.

WHY POM?
    Locators and actions belong here — not in the test file.
    Tests become readable English. Selenium mechanics stay hidden.
    When the UI changes, you fix ONE place, not every test method.

Pattern:
    - Locators class: all By selectors as class-level constants
    - UrbanRoutesPage class: all user actions as methods
    - Tests call page methods, never touch raw Selenium directly
"""

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from config import TIMEOUTS

logger = logging.getLogger(__name__)


class Locators:
    """All CSS/XPath selectors for Urban Routes in one place."""

    FROM_FIELD          = (By.ID, "from")
    TO_FIELD            = (By.ID, "to")
    COMFORT_TARIFF      = (By.XPATH, "//div[contains(@class,'tcard') and .//div[text()='Comfort']]")
    PHONE_BUTTON        = (By.CLASS_NAME, "np-button")
    PHONE_INPUT         = (By.ID, "phone")
    PHONE_NEXT_BUTTON   = (By.XPATH, "//button[text()='Next']")
    SMS_CODE_INPUT      = (By.ID, "code")
    SMS_CONFIRM_BUTTON  = (By.XPATH, "//button[text()='Confirm']")
    PAYMENT_METHOD      = (By.CLASS_NAME, "pp-button")
    ADD_CARD_BUTTON     = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_INPUT   = (By.ID, "number")
    CARD_CVV_INPUT      = (By.XPATH, "//input[@placeholder='12']")
    PAYMENT_SAVE_BUTTON = (By.XPATH, "//button[text()='Link']")
    CLOSE_PAYMENT       = (By.XPATH, "//button[@class='close-button section-close']")
    DRIVER_COMMENT      = (By.ID, "comment")
    BLANKET_TOGGLE      = (By.XPATH, "//div[text()='Blanket and handkerchiefs']/following-sibling::div//input[@type='checkbox']")
    ICE_CREAM_PLUS      = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-plus']")
    ICE_CREAM_COUNT     = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-value']")
    ORDER_TAXI_BUTTON   = (By.CLASS_NAME, "smart-button")
    ORDER_HEADER        = (By.CLASS_NAME, "order-header-title")
    DRIVER_INFO         = (By.CLASS_NAME, "order-header-content")


class UrbanRoutesPage:
    """
    Encapsulates all user interactions with the Urban Routes web application.
    Usage: page = UrbanRoutesPage(driver)
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUTS["explicit"])
        self.long_wait = WebDriverWait(driver, TIMEOUTS["driver_info"])

    def _find(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def set_route(self, from_address: str, to_address: str) -> None:
        logger.info(f"Setting route: {from_address} → {to_address}")
        f = self._find(Locators.FROM_FIELD); f.clear(); f.send_keys(from_address)
        t = self._find(Locators.TO_FIELD); t.clear(); t.send_keys(to_address)

    def get_from_address(self) -> str:
        return self._find_visible(Locators.FROM_FIELD).get_attribute("value")

    def get_to_address(self) -> str:
        return self._find_visible(Locators.TO_FIELD).get_attribute("value")

    def select_comfort_tariff(self) -> None:
        logger.info("Selecting Comfort tariff")
        self._find(Locators.COMFORT_TARIFF).click()

    def get_selected_tariff_name(self) -> str:
        el = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'tcard') and contains(@class,'active')]//div[@class='tcard-title']")
        ))
        return el.text

    def add_phone_number(self, phone: str, sms_code: str) -> None:
        logger.info(f"Adding phone: {phone}")
        self._find(Locators.PHONE_BUTTON).click()
        pi = self._find(Locators.PHONE_INPUT); pi.clear(); pi.send_keys(phone)
        self._find(Locators.PHONE_NEXT_BUTTON).click()
        si = self._find(Locators.SMS_CODE_INPUT); si.clear(); si.send_keys(sms_code)
        self._find(Locators.SMS_CONFIRM_BUTTON).click()

    def get_phone_number_displayed(self) -> str:
        return self._find_visible(Locators.PHONE_BUTTON).text

    def add_credit_card(self, card_number: str, cvv: str) -> None:
        logger.info("Adding credit card")
        self._find(Locators.PAYMENT_METHOD).click()
        self._find(Locators.ADD_CARD_BUTTON).click()
        ci = self._find(Locators.CARD_NUMBER_INPUT); ci.clear(); ci.send_keys(card_number)
        cv = self._find(Locators.CARD_CVV_INPUT); cv.send_keys(cvv); cv.send_keys("\t")
        self._find(Locators.PAYMENT_SAVE_BUTTON).click()
        self._find(Locators.CLOSE_PAYMENT).click()

    def add_driver_comment(self, comment: str) -> None:
        f = self._find(Locators.DRIVER_COMMENT); f.clear(); f.send_keys(comment)

    def get_driver_comment(self) -> str:
        return self._find_visible(Locators.DRIVER_COMMENT).get_attribute("value")

    def toggle_blanket(self) -> None:
        self._find(Locators.BLANKET_TOGGLE).click()

    def is_blanket_checked(self) -> bool:
        return self._find_visible(Locators.BLANKET_TOGGLE).is_selected()

    def increment_ice_cream(self, times: int = 1) -> None:
        for _ in range(times):
            self._find(Locators.ICE_CREAM_PLUS).click()

    def get_ice_cream_count(self) -> int:
        return int(self._find_visible(Locators.ICE_CREAM_COUNT).text)

    def place_order(self) -> None:
        self._find(Locators.ORDER_TAXI_BUTTON).click()

    def is_order_modal_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(Locators.ORDER_HEADER))
            return True
        except Exception:
            return False

    def wait_for_driver_info(self) -> bool:
        logger.info("Waiting for driver info panel")
        try:
            self.long_wait.until(EC.visibility_of_element_located(Locators.DRIVER_INFO))
            return True
        except Exception:
            logger.warning("Driver info did not appear within timeout")
            return False
