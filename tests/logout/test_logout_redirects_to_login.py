from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_logout_redirects_to_login(driver, logged_in_user):
    """
    Verify that after logout user is redirected to login page.

    PRECONDITIONS:
        - User must be logged in

    ACTION:
        - Click on user dropdown button (contains email and dropdown icon)
        - Wait for logout button to appear in dropdown menu
        - Click on logout button

    CHECK:
        - User is redirected to login page immediately after logout
    """
    with DashboardPage(driver) as dashboard_page:
        # Step 1: Click user dropdown button
        dashboard_page.click_user_dropdown()

        # Step 2: Wait for logout button to appear
        expect(dashboard_page.logout_button).to_be_visible()

        # Step 3: Click logout button
        dashboard_page.click_logout()

        # Wait for page to load after logout
        dashboard_page.page.wait_for_load_state("load")

    # Verify logout successful - check redirect to login page
    with LoginPage(driver) as login_page:
        # Verify we are on login page
        expect(login_page.page).to_have_url(login_page.url)
