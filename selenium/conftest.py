# conftest.py — Shared pytest fixtures for Sprint 8 Selenium tests
# Fixtures defined here are automatically discovered by pytest for all
# tests in the selenium/ directory without needing explicit imports.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# NOTE: This URL is a TripleTen sandbox endpoint. It is not publicly
# accessible outside the TripleTen course environment. Tests will
# fail with a connection error unless run inside that sandbox.
URBAN_ROUTES_URL = "https://cnt-1234567890.containerhub.tripleten-services.com"


@pytest.fixture(scope="class")
def driver():
    """Spin up a Chrome WebDriver instance for the test class, then quit."""
    opts = Options()
    opts.add_argument("--window-size=1280,800")
    drv = webdriver.Chrome(options=opts)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


@pytest.fixture(scope="class", autouse=True)
def open_url(driver):
    """Navigate to the Urban Routes app before each test class runs."""
    driver.get(URBAN_ROUTES_URL)
    yield
