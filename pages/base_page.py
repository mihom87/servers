from playwright.sync_api import Page
from typing import Optional
from utils.webdriver import WebDriver


class BasePage:
    """
    Base class for all pages in Page Object pattern.
    """

    def __init__(self, driver: WebDriver, path: str, timeout: int = 30000):
        """
        Initialize base page.

        Args:
            driver: WebDriver instance (wrapper over playwright)
            path: Page path that will be appended to base_url
            timeout: Wait timeout in milliseconds (default 30 seconds)
        """
        self.driver = driver
        self.path = path
        self.url = self.driver.base_url + path
        self.timeout = timeout
        self._page: Optional[Page] = driver.page

    @property
    def page(self) -> Optional[Page]:
        """Get playwright page object"""
        return self._page

    def wait_for_load_state(self, state: str = "load", **kwargs):
        """Wait for page load state"""
        if self._page:
            self._page.wait_for_load_state(state, timeout=self.timeout, **kwargs)

    def get_url(self) -> str:
        """Get current URL"""
        if self._page:
            return self._page.url
        return ""

    def goto(self, **kwargs):
        """
        Open page by saved URL.

        Args:
            **kwargs: Additional parameters for page.goto() (wait_until, timeout, etc.)
        """
        if self._page:
            self._page.goto(self.url, **kwargs)
            self.wait_for_load_state()

    def __enter__(self):
        """Enter context manager"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager"""
        return
