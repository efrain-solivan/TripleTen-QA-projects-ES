"""
conftest.py — Shared pytest fixtures for the Urban Routes test suite.

This file is auto-loaded by pytest. No imports needed in test files.

Fixtures provided:
    driver      — Chrome WebDriver instance (function-scoped: fresh browser per test)
    page        — UrbanRoutesPage instance pre-navigated to BASE_URL
    screenshot  — Auto-captures screenshot to /screenshots on test failure

Logging:
    Set LOG_LEVEL env var to DEBUG for verbose selenium output.
"""

import os
import sys
import logging
import pytest
from datetime import datetime

# ─── Path fix ────────────────────────────────────────────────────────────────────────────────
# The test folder is named 'selenium/' which would shadow the selenium library
# on import. We explicitly add both the repo root and this folder to sys.path
# so that:
#   - 'from config import ...'      resolves to  repo_root/config.py
#   - 'from pages import ...'       resolves to  selenium/pages/
#   - 'from selenium import ...'    resolves to  the installed selenium library
_HERE = os.path.dirname(os.path.abspath(__file__))          # .../selenium/
_ROOT = os.path.dirname(_HERE)                               # repo root
for _p in (_ROOT, _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from selenium import webdriver                               # library — now unambiguous
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from config import BASE_URL, SCREENSHOTS_DIR
from pages.urban_routes_page import UrbanRoutesPage          # local pages/ folder

# ─── Logging ──────────────────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger("conftest")


# ─── Screenshot directory ───────────────────────────────────────────────────────────────

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


# ─── WebDriver Fixture ──────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def driver():
    """
    Provide a configured Chrome WebDriver instance.

    Scope: function — each test gets a clean browser session.
    Teardown: browser quits after every test, pass or fail.

    Chrome options:
        --headless=new  : for CI environments (no display)
        --no-sandbox    : required in Docker/GitHub Actions
        --window-size   : consistent viewport for all tests
    """
    logger.info("Starting Chrome WebDriver")

    options = Options()

    # Use headless mode in CI; set HEADLESS=false locally to watch tests run
    if os.getenv("HEADLESS", "true").lower() != "false":
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")

    _driver = webdriver.Chrome(options=options)
    _driver.implicitly_wait(0)  # Keep at 0 — explicit waits only

    yield _driver

    logger.info("Quitting Chrome WebDriver")
    _driver.quit()


# ─── Page Fixture ──────────────────────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def page(driver):
    """
    Navigate to BASE_URL and return a ready UrbanRoutesPage instance.

    Depends on: driver fixture
    """
    logger.info(f"Navigating to {BASE_URL}")
    driver.get(BASE_URL)
    return UrbanRoutesPage(driver)


# ─── Screenshot on Failure ────────────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook: capture a screenshot automatically when a test fails.

    File saved to: screenshots/FAIL_<test_name>_<timestamp>.png
    These are uploaded as CI artifacts by the GitHub Actions workflow.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"FAIL_{item.name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            try:
                driver.save_screenshot(filepath)
                logger.warning(f"Screenshot saved: {filepath}")
            except Exception as e:
                logger.error(f"Could not save screenshot: {e}")
