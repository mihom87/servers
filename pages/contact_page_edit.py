from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator
import re


class ContactPageEdit(BasePage):
    """
    Contact page edit class after successful login.
    """

    path = re.compile(r".*/a:0m5Nx6dn/account/contact/\d+/edit$")

    def __init__(self, driver: WebDriver):
        """
        Initialize contact page edit.

        Args:
            driver: WebDriver instance
        """
        # Call super with empty string since path is regex, not a string
        super().__init__(driver, "")
        # Override path with regex pattern
        self.path = self.__class__.path

    # Locators
    @property
    def first_name_input(self) -> Locator:
        return self.page.locator("#contactFields").locator('input[name="fname"]')

    @property
    def last_name_input(self) -> Locator:
        return self.page.locator("#contactFields").locator('input[name="lname"]')

    @property
    def job_title_input(self) -> Locator:
        return self.page.locator("#contactFields").locator('input[name="tokens.title"]')

    @property
    def email_input(self) -> Locator:
        return self.page.locator("#contactFields").locator('input[name="email"]')

    @property
    def phone_number_input(self) -> Locator:
        return self.page.locator("#contactFields").locator('input[name="phone_number"]')

    @property
    def secondary_email_input(self) -> Locator:
        return self.page.locator("#contactFields").locator('input[name="email2"]')

    @property
    def comment_textarea(self) -> Locator:
        return self.page.locator("#contactFields").locator(
            'textarea[placeholder="Enter comment"]'
        )

    @property
    def primary_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role(
            "checkbox", name="Primary", exact=True
        )

    @property
    def technical_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role(
            "checkbox", name="Technical", exact=True
        )

    @property
    def billing_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role(
            "checkbox", name="Billing", exact=True
        )

    @property
    def abuse_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role(
            "checkbox", name="Abuse", exact=True
        )

    @property
    def emergency_checkbox(self) -> Locator:
        return self.page.locator("#role").get_by_role(
            "checkbox", name="Emergency", exact=True
        )

    @property
    def save_button(self) -> Locator:
        return self.page.get_by_role("button", name="Save", exact=True)

    # Actions
    def fill_first_name(self, value: str):
        self.first_name_input.fill(value)

    def fill_last_name(self, value: str):
        self.last_name_input.fill(value)

    def fill_job_title(self, value: str):
        self.job_title_input.fill(value)

    def fill_email(self, value: str):
        self.email_input.fill(value)

    def fill_phone_number(self, value: str):
        self.phone_number_input.fill(value)

    def fill_secondary_email(self, value: str):
        self.secondary_email_input.fill(value)

    def fill_comment(self, value: str):
        self.comment_textarea.fill(value)

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

    def click_save_button(self):
        self.save_button.click()
