from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator


class DashboardPage(BasePage):
    """
    Dashboard page class after successful login.
    """

    path = "/a:0m5Nx6dn/dashboard"

    def __init__(self, driver: WebDriver):
        """
        Initialize dashboard page.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver, self.__class__.path)

    # Locators
    @property
    def user_dropdown_button(self) -> Locator:
        """
        User dropdown button that contains email and dropdown icon.
        """
        return self.page.locator(
            '//button[.//span[@title="qa+aqa@servers.com"] and .//*[@id="Icon/Dropdown"]]'
        )

    @property
    def logout_button(self) -> Locator:
        """
        Logout button in dropdown menu.
        """
        return self.page.locator(
            '//ul[@role="presentation"]/li/button[.//span[text()="Logout"]]'
        )

    @property
    def account_link(self) -> Locator:
        """
        Account link in dropdown menu.
        """
        return self.page.locator(
            '//ul[@role="presentation"]/li/a[@href="/a:0m5Nx6dn/account"]'
        )

    # Actions
    def click_user_dropdown(self):
        """Click user dropdown button to open menu."""
        self.user_dropdown_button.click()

    def click_logout(self):
        """Click logout button."""
        self.logout_button.click()

    def click_account(self):
        """Click account button."""
        self.account_link.click()
