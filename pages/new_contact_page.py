from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator


class NewContactPage(BasePage):
    """
    New contact page class for adding contacts.
    """

    path = "/a:0m5Nx6dn/account/new-contact"

    def __init__(self, driver: WebDriver):
        """
        Initialize new contact page.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver, self.__class__.path)


    @property
    def create_button(self) -> Locator:
        """
        Account link in dropdown menu.
        """
        return self.page.locator('button[type="submit"][role="button"][title="Create"]')
    
    @property
    def first_name_input(self) -> Locator:
        """
        First name input.
        """
        return self.page.locator("#contactFields").get_by_label("First name", exact=True)
    
    @property
    def last_name_input(self) -> Locator:
        """
        Last name input.
        """
        return self.page.locator("#contactFields").get_by_label("Last name", exact=True)
    
    @property
    def job_title_input(self) -> Locator:
        """
        Job title input.
        """
        return self.page.locator("#contactFields").get_by_label("Job title", exact=True)
    
    @property
    def email_input(self) -> Locator:
        """
        Email input.
        """
        return self.page.locator("#contactFields").get_by_label("Email", exact=True)

    @property
    def phone_number_input(self) -> Locator:
        """
        Phone input.
        """
        return self.page.locator("#contactFields").get_by_label("Phone number", exact=True)
    
    @property
    def secondary_email_input(self) -> Locator:
        """
        Secondary email input.
        """
        return self.page.locator("#contactFields").get_by_label("Secondary email", exact=True)
    
    @property
    def comment_textarea(self) -> Locator:
        """
        Comment input.
        """
        return self.page.locator("#contactFields").get_by_placeholder("Enter comment", exact=True)
    
    @property
    def primary_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role("checkbox", name="Primary", exact=True)

    @property
    def technical_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role("checkbox", name="Technical", exact=True)

    @property
    def billing_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role("checkbox", name="Billing", exact=True)

    @property
    def abuse_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role("checkbox", name="Abuse", exact=True)

    @property
    def emergency_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role("checkbox", name="Emergency", exact=True)
    
    # Actions
    def click_primary_checkbox(self):
        self.primary_checkbox.click()

    def click_technical_checkbox(self):
        self.technical_checkbox.click()

    def click_billing_checkbox(self):
        self.billing_checkbox.click()

    def click_abuse_checkbox(self):
        self.abuse_checkbox.click()

    def click_emergency_checkbox(self):
        self.emergency_checkbox.click()