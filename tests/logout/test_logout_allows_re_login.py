import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.custom_expect import expect


@pytest.fixture
def logged_out_user(driver, logged_in_user):
    """
    Logout user after login.

    """
    # Perform logout
    with DashboardPage(driver) as dashboard_page:
        # Click user dropdown button
        dashboard_page.click_user_dropdown()

        # Wait for logout button to appear
        expect(dashboard_page.logout_button).to_be_visible()

        # Click logout button
        dashboard_page.click_logout()

        # Wait for page to load after logout
        dashboard_page.page.wait_for_load_state("load")

    # Verify logout successful - check redirect to login page
    with LoginPage(driver) as login_page:
        # Verify we are on login page
        expect(login_page.page).to_have_url(login_page.url)

    # User is now logged out, driver state is modified


def test_logout_allows_re_login(driver, logged_out_user):
    """
    Verify that after logout user can successfully log in again.

    PRECONDITIONS:
        - User must be logged out (done by logged_out_user fixture)

    ACTION:
        - Attempt to log in with valid credentials

    CHECK:
        - User can successfully log in again
        - User is redirected to dashboard after successful login
    """
    # Attempt to log in again
    with LoginPage(driver) as login_page:
        # Wait for login form fields to be visible
        expect(login_page.email_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()

        # Fill credentials
        login_page.fill_email("day+test9@servers.com")
        login_page.fill_password("Twz8pyE5B9Y3")

        # Click login button
        login_page.click_login()

        # Wait for page to load
        login_page.page.wait_for_load_state("load")

    # Verify successful login after logout
    with DashboardPage(driver) as dashboard_page:
        # Verify we are on dashboard page
        expect(dashboard_page.page).to_have_url(dashboard_page.url)

        # Wait for dashboard elements to appear
        expect(dashboard_page.user_dropdown_button).to_be_visible()
