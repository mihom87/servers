"""
Test for successful login with valid credentials.

Test file: test_successful_login_with_valid_credentials.py
"""

from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_successful_login_with_valid_credentials(driver, opened_login_page):
    """
    Verify that user can successfully log in with valid email and password.

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page
        - Login form should open automatically

    ACTION:
        - Enter valid email address in the email field
        - Enter valid password in the password field
        - Click on Login button

    CHECK:
        - User is successfully authenticated
        - User is redirected to the dashboard or home page
        - Success message or user profile is displayed
    """
    with LoginPage(driver) as login_page:
        # Fill credentials
        login_page.fill_email("day+test9@servers.com")
        login_page.fill_password("Twz8pyE5B9Y3")

        # Click login button
        login_page.click_login()

        # Wait for page to load
        login_page.page.wait_for_load_state("load")

        # Verify we are on dashboard page
        expect(login_page.page).to_have_url(
            "https://portal.servers.com/a:0m5Nx6dn/dashboard"
        )

        # Wait for dashboard elements to appear
        login_page.page.wait_for_selector('[id="Icon/Card"]', state="visible")
