from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator


class LoginPage(BasePage):
    """
    Login page class for authentication functionality.
    """

    path = "/login"

    def __init__(self, driver: WebDriver):
        """
        Initialize login page.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver, self.__class__.path)

    # Locators
    @property
    def email_input(self) -> Locator:
        """Email input field."""
        return self.page.locator("#email")

    @property
    def password_input(self) -> Locator:
        """Password input field."""
        return self.page.locator("#password")

    @property
    def login_button(self) -> Locator:
        """Login submit button."""
        return self.page.locator("//button[@type='submit']")

    @property
    def email_error_icon(self) -> Locator:
        """Error icon for email field."""
        # Building xpath from email field parent to find the specific error icon
        return self.page.locator(
            "//input[@id='email']/following-sibling::*[@id='Icon/Attention'] | //input[@id='email']/..//*[@id='Icon/Attention']"
        )

    @property
    def password_error_icon(self) -> Locator:
        """Error icon for password field."""
        # Building xpath from password field parent to find the specific error icon
        return self.page.locator(
            "//input[@id='password']/following-sibling::*[@id='Icon/Attention'] | //input[@id='password']/..//*[@id='Icon/Attention']"
        )

    @property
    def auth_failed_message(self) -> Locator:
        """Authentication failed error message."""
        return self.page.locator("#auth_failed")

    # Actions
    def fill_email(self, email: str, delay: int = 50):
        """
        Fill email input field by simulating user typing.

        Args:
            email: Email address to enter
            delay: Delay between keystrokes in milliseconds (default: 50ms)
        """
        self.email_input.press_sequentially(email, delay=delay)

    def fill_password(self, password: str, delay: int = 50):
        """
        Fill password input field by simulating user typing.

        Args:
            password: Password to enter
            delay: Delay between keystrokes in milliseconds (default: 50ms)
        """
        self.password_input.press_sequentially(password, delay=delay)

    def click_login(self):
        """Click login button."""
        self.login_button.click()
