import pytest
from playwright.sync_api import sync_playwright
from utils.webdriver import WebDriver


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture for creating browser driver (wrapper around playwright).
    Returns WebDriver instance.
    """
    # Get parameters from pytest options
    base_url = request.config.getoption("--base-url")
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    playwright = sync_playwright().start()
    web_driver = WebDriver(playwright, base_url=base_url, browser_type=browser)

    # Launch browser and create page
    web_driver.launch_browser(headless=headless)
    web_driver.new_context()
    web_driver.new_page()

    yield web_driver

    # Close browser after test
    web_driver.close()
    playwright.stop()


def pytest_addoption(parser):
    """Add command line options"""
    parser.addoption(
        "--base-url",
        action="store",
        required=True,
        help="Base URL for the application under test",
    )
    parser.addoption(
        "--browser",
        action="store",
        required=True,
        choices=["chromium"],
        help="Browser type to use for tests (currently only chromium is supported)",
    )
    parser.addoption(
        "--no-headless",
        action="store_false",
        dest="headless",
        default=True,
        help="Run browser in visible mode (by default runs in headless mode)",
    )
