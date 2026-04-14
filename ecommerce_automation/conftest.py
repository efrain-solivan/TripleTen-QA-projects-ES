import pytest
import undetected_chromedriver as uc


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="false",
                     help="Run Chrome headless: true or false (default: false)")
    parser.addoption("--base-url", action="store", default="https://www.jomashop.com")


@pytest.fixture(scope="session")
def driver(request):
    # undetected_chromedriver patches out every automation fingerprint that
    # PerimeterX and similar bot-detection systems look for — navigator.webdriver,
    # chrome.runtime, CDP exposure, and more. It is a drop-in replacement for
    # selenium.webdriver.Chrome and accepts the same options/calls.
    headless = request.config.getoption("--headless").lower() == "true"

    options = uc.ChromeOptions()
    options.add_argument("--window-size=1400,900")
    options.add_argument("--lang=en-US")

    driver = uc.Chrome(options=options, headless=headless, use_subprocess=True, version_main=146)
    driver.implicitly_wait(0)

    yield driver

    # Neutralise undetected_chromedriver's __del__ before we call quit().
    # Without this, Python's GC calls __del__ → quit() a second time after our
    # fixture already closed the browser, producing OSError [WinError 6] on Windows.
    # Replacing __del__ with a no-op prevents the double-quit entirely.
    try:
        driver.__class__.__del__ = lambda self: None
    except Exception:
        pass

    try:
        driver.quit()
    except OSError:
        pass


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")
