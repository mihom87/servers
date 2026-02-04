from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator


class AccountPage(BasePage):
    """
    Account page class.
    """

    path = "/a:0m5Nx6dn/account"

    def __init__(self, driver: WebDriver):
        """
        Initialize account page.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver, self.__class__.path)

    @property
    def account_link(self) -> Locator:
        """
        Account link in dropdown menu.

        Element a with href to account page, has span in children.
        """
        return self.page.locator(
            '//a[@type="button" and @role="button" and @title="Create"]'
        )
    
    # Actions
    def click_create_contact(self):
        """Click create account button."""
        self.account_link.click()
