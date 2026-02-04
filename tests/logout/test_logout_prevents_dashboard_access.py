from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_logout_prevents_dashboard_access(driver, logged_in_user):
    """
    Verify that after logout user cannot access dashboard and is redirected to login.

    PRECONDITIONS:
        - User must be logged in

    ACTION:
        - Perform logout
        - Attempt to navigate to dashboard page

    CHECK:
        - User is redirected to login page when trying to access dashboard
        - Dashboard is not accessible after logout
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

    # Attempt to access dashboard - should redirect to login
    with DashboardPage(driver) as dashboard_page:
        dashboard_page.goto()

        # Wait for potential redirect
        dashboard_page.page.wait_for_load_state("load")

    # Verify redirect to login page
    with LoginPage(driver) as login_page:
        # Verify we are redirected to login page
        expect(login_page.page).to_have_url(login_page.url)
