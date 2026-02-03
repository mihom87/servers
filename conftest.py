import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
from filelock import FileLock, Timeout
from utils.webdriver import WebDriver


# Storage paths (relative to project root)
PROJECT_ROOT = Path(__file__).parent
STORAGE_DIR = PROJECT_ROOT / "storage"
STORAGE_FILE = STORAGE_DIR / "auth_storage.json"
LOCK_FILE = STORAGE_DIR / "auth_storage.json.lock"


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture for creating browser driver (wrapper around playwright).
    Automatically creates and loads storage with cookie consent on first run.
    Safe for pytest-xdist parallel execution using file locking.

    Returns WebDriver instance with pre-loaded storage (cookie consent).
    """
    # Get parameters from pytest options
    base_url = request.config.getoption("--base-url")
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("headless")

    playwright = sync_playwright().start()
    web_driver = WebDriver(playwright, base_url=base_url, browser_type=browser)
    web_driver.launch_browser(headless=headless)

    # === CREATE STORAGE IF NOT EXISTS (safe for xdist) ===
    # Ensure storage directory exists before creating lock
    STORAGE_DIR.mkdir(exist_ok=True)

    try:
        with FileLock(str(LOCK_FILE), timeout=60):
            # Double-check pattern: verify again inside lock
            if not STORAGE_FILE.exists():
                try:
                    # Create temporary context to generate storage
                    web_driver.new_context()
                    web_driver.new_page()

                    # Open non-existent page to minimize side-effects
                    # Cookie popup appears on all pages including 404
                    web_driver.goto("/404")
                    web_driver.page.wait_for_load_state("load")

                    # Wait for cookie popup to appear and be visible
                    popup_locator = web_driver.page.locator("div.cky-consent-bar")
                    expect(popup_locator).to_be_visible(timeout=10000)

                    # Click Accept button (automatically waits for clickable state)
                    accept_button = web_driver.page.locator(
                        'div.cky-consent-bar button[aria-label="Accept"]'
                    )
                    accept_button.click()

                    # Wait for cookies to be set
                    web_driver.page.wait_for_timeout(1000)

                    # Save storage state
                    web_driver.context.storage_state(path=str(STORAGE_FILE))

                finally:
                    # Close temporary context
                    web_driver.context.close()

    except Timeout:
        raise RuntimeError(
            f"Could not acquire lock for {LOCK_FILE} within 60 seconds. "
            "Another worker might be stuck."
        )
    except Exception as e:
        # Clean up corrupted file on error
        if STORAGE_FILE.exists():
            STORAGE_FILE.unlink()
        raise RuntimeError(f"Failed to create storage: {e}") from e

    # === CREATE MAIN CONTEXT WITH STORAGE ===
    web_driver.new_context(storage_state=str(STORAGE_FILE))
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
