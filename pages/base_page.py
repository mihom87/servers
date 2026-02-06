from playwright.sync_api import Page
from typing import Optional
from utils.webdriver import WebDriver
from components.side_menu import SideMenu


class BasePage:
    """
    Base class for all pages in Page Object pattern.
    """

    # Default timeouts (can be overridden in child classes)
    action_timeout: int = 30000  # Timeout for actions (click, fill, etc.)
    navigation_timeout: int = 30000  # Timeout for navigation (goto)
    expect_timeout: int = 5000  # Timeout for expect assertions

    def __init__(self, driver: WebDriver, path: str):
        """
        Initialize base page.

        Args:
            driver: WebDriver instance (wrapper over playwright)
            path: Page path that will be appended to base_url
        """
        self.driver = driver
        self.path = path
        self.url = self.driver.base_url + path

        # Apply timeouts if page already exists
        self._apply_timeouts()

    def _apply_timeouts(self):
        """Apply default timeouts to current page"""
        if self.driver.page:
            self.driver.page.set_default_timeout(self.action_timeout)
            self.driver.page.set_default_navigation_timeout(self.navigation_timeout)

    @property
    def page(self) -> Optional[Page]:
        """Get current page from driver"""
        return self.driver.page
    
    @property
    def side_menu(self) -> SideMenu:
        """Get side menu from page"""
        return SideMenu(
            self.page.get_by_role("link", name="Servers.com").locator(
                "xpath=ancestor::*[@role='region'][1]"
            )
        )

    def wait_for_load_state(self, state: str = "load", **kwargs):
        """Wait for page load state"""
        if self.page:
            self.page.wait_for_load_state(state, **kwargs)

    def get_url(self) -> str:
        """Get current URL"""
        if self.page:
            return self.page.url
        return ""

    def goto(self, **kwargs):
        """
        Open page by saved URL.

        Args:
            **kwargs: Additional parameters for page.goto() (wait_until, timeout, etc.)
        """
        # Apply timeouts before navigation (ensures timeouts for new page)
        self._apply_timeouts()

        if self.page:
            self.page.goto(self.url, **kwargs)
            self.wait_for_load_state()
    @property
    def not_found_text(self):
        return self.page.get_by_text("The page wasn't found.", exact=False)


    def __enter__(self):
        """Enter context manager"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager"""
        return
