import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


@pytest.fixture
def logged_in_user(driver):
    """
    Login user with valid credentials.

    This fixture performs login and ensures user is authenticated.
    After this fixture, user is logged in and ready for tests that require authentication.

    Args:
        driver: WebDriver fixture from conftest.py
    """
    with LoginPage(driver) as login_page:
        login_page.goto()

        # Wait for login form fields to be visible
        expect(login_page.email_input).to_be_visible(timeout=20000)
        expect(login_page.password_input).to_be_visible(timeout=20000)

        # Fill credentials
        login_page.fill_email("day+test9@servers.com")
        login_page.fill_password("Twz8pyE5B9Y3")

        # Click login button
        login_page.click_login()

        # Wait for page to load
        login_page.page.wait_for_load_state("load")

    # Verify login successful using DashboardPage
    with DashboardPage(driver) as dashboard_page:
        # Verify we are on dashboard page (login successful)
        expect(dashboard_page.page).to_have_url(dashboard_page.url)

        # Wait for dashboard logout elements to appear
        expect(dashboard_page.user_dropdown_button).to_be_visible()
