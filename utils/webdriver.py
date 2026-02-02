from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    Error as PlaywrightError,
)
from typing import Optional
import functools


def handle_element_errors(func):
    """Decorator for handling element interaction errors.
    Catches only Playwright errors (Error and its subclasses) and converts them to AssertionError.
    RuntimeError and other system errors are not caught.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except PlaywrightError as e:
            # Catch only Playwright errors (Error, TimeoutError, etc.)
            raise AssertionError(f"Element interaction failed: {e}") from e
        # All other exceptions (RuntimeError, etc.) are re-raised as-is

    return wrapper


class WebDriver:
    """
    Wrapper around playwright driver for future integration with reporting system.
    All driver methods are duplicated through wrappers.
    """

    def __init__(
        self,
        playwright_driver: Playwright,
        base_url: str,
        browser_type: str = "chromium",
    ):
        """
        Initialize wrapper around playwright driver.

        Args:
            playwright_driver: Playwright instance from playwright
            base_url: Base URL prefix (e.g., 'https://example.com')
            browser_type: Browser type ('chromium', 'firefox', 'webkit')
        """
        self._driver = playwright_driver
        self._base_url = base_url
        self._browser_type = browser_type
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None

    def launch_browser(self, **kwargs):
        """Launch browser"""
        browser_launcher = getattr(self._driver, self._browser_type)
        self._browser = browser_launcher.launch(**kwargs)
        return self._browser

    def new_context(self, **kwargs):
        """Create new context"""
        if not self._browser:
            raise RuntimeError("Browser must be launched first")
        self._context = self._browser.new_context(**kwargs)
        return self._context

    def new_page(self, **kwargs):
        """Create new page"""
        if not self._context:
            self.new_context()
        self._page = self._context.new_page(**kwargs)
        return self._page

    def goto(self, url: str, **kwargs):
        """
        Navigate to URL with base URL prefix.

        Args:
            url: Relative URL that will be appended to base_url
        """
        if not self._page:
            raise RuntimeError("Page must be created first")

        full_url = f"{self._base_url}{url}"
        return self._page.goto(full_url, **kwargs)

    @property
    def page(self) -> Optional[Page]:
        """Get current page"""
        return self._page

    @property
    def context(self) -> Optional[BrowserContext]:
        """Get current context"""
        return self._context

    @property
    def browser(self) -> Optional[Browser]:
        """Get browser"""
        return self._browser

    def close(self):
        """Close browser"""
        if self._page:
            self._page.close()
        if self._context:
            self._context.close()
        if self._browser:
            self._browser.close()

    # Delegating page methods for convenience
    @handle_element_errors
    def click(self, selector: str, **kwargs):
        """Click on element"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.click(selector, **kwargs)

    @handle_element_errors
    def fill(self, selector: str, value: str, **kwargs):
        """Fill field"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.fill(selector, value, **kwargs)

    def locator(self, selector: str):
        """Get locator"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.locator(selector)

    @handle_element_errors
    def wait_for_selector(self, selector: str, **kwargs):
        """Wait for element to appear"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.wait_for_selector(selector, **kwargs)

    @handle_element_errors
    def press(self, selector: str, key: str, **kwargs):
        """Press key on element"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.press(selector, key, **kwargs)

    @handle_element_errors
    def select_option(self, selector: str, value: str, **kwargs):
        """Select option in select"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.select_option(selector, value, **kwargs)

    @handle_element_errors
    def check(self, selector: str, **kwargs):
        """Check checkbox"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.check(selector, **kwargs)

    @handle_element_errors
    def uncheck(self, selector: str, **kwargs):
        """Uncheck checkbox"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.uncheck(selector, **kwargs)

    @handle_element_errors
    def hover(self, selector: str, **kwargs):
        """Hover over element"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.hover(selector, **kwargs)

    @handle_element_errors
    def dblclick(self, selector: str, **kwargs):
        """Double click"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.dblclick(selector, **kwargs)

    @handle_element_errors
    def type(self, selector: str, text: str, **kwargs):
        """Type text (with delays between characters)"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.type(selector, text, **kwargs)

    def get_text(self, selector: str, **kwargs):
        """Get element text"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.locator(selector).text_content(**kwargs)

    def get_attribute(self, selector: str, name: str, **kwargs):
        """Get element attribute"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.locator(selector).get_attribute(name, **kwargs)

    def is_visible(self, selector: str, **kwargs):
        """Check element visibility"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.locator(selector).is_visible(**kwargs)

    def is_enabled(self, selector: str, **kwargs):
        """Check element enabled state"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.locator(selector).is_enabled(**kwargs)

    def wait_for_load_state(self, state: str = "load", **kwargs):
        """Wait for page load state"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.wait_for_load_state(state, **kwargs)

    def reload(self, **kwargs):
        """Reload page"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.reload(**kwargs)

    def go_back(self, **kwargs):
        """Go back in browser history"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.go_back(**kwargs)

    def go_forward(self, **kwargs):
        """Go forward in browser history"""
        if not self._page:
            raise RuntimeError("Page must be created first")
        return self._page.go_forward(**kwargs)
