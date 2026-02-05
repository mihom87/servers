from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator
import re


class ContactPage(BasePage):
    """
    Contact page class after successful login.
    """

    path = re.compile(r".*/a:0m5Nx6dn/account/contact/\d+$")

    def __init__(self, driver: WebDriver):
        """
        Initialize contact page.

        Args:
            driver: WebDriver instance
        """
        # Call super with empty string since path is regex, not a string
        super().__init__(driver, "")
        # Override path with regex pattern
        self.path = self.__class__.path

    def _value_locator_near_label(self, label: Locator) -> Locator:
        return label.locator("xpath=..").locator("> div").nth(1)

    # Locators
    @property
    def edit_button(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_role("button", name="Edit", exact=True)


    # Labels
    @property
    def first_name_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "First name", exact=True
        )

    @property
    def last_name_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Last name", exact=True
        )

    @property
    def email_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Email", exact=True
        )

    @property
    def secondary_email_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Secondary email", exact=True
        )

    @property
    def phone_number_label(self):  # картинка!
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Phone number", exact=True
        )

    @property
    def role_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Role", exact=True
        )

    @property
    def job_title_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Job title", exact=True
        )

    @property
    def comments_label(self):
        return self.page.locator('div:has(h2:has-text("Contact info"))').get_by_text(
            "Comments", exact=True
        )

    # Values
    @property
    def first_name_value(self):
        return (
            self._value_locator_near_label(self.first_name_label)
        )

    @property
    def last_name_value(self):
        return (
            self._value_locator_near_label(self.last_name_label)
        )

    @property
    def email_value(self):
        return (
            self._value_locator_near_label(self.email_label)
        )

    @property
    def secondary_email_value(self):
        return (
            self
            ._value_locator_near_label(self.secondary_email_label)
        )

    @property
    def phone_number_value(self):
        return (
            self._value_locator_near_label(self.phone_number_label)
        )

    @property
    def role_value(self):
        return self._value_locator_near_label(self.role_label)

    @property
    def job_title_value(self):
        return self._value_locator_near_label(self.job_title_label)

    @property
    def comments_value(self):
        return (
            self._value_locator_near_label(self.comments_label)
        )
    
    # Actions
    def click_edit_button(self):
        self.edit_button.click()
