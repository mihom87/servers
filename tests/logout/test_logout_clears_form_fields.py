from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_logout_clears_form_fields(driver, logged_in_user):
    """
    Verify that after logout login form fields are cleared and error icons are not visible.

    PRECONDITIONS:
        - User must be logged in

    ACTION:
        - Click on user dropdown button (contains email and dropdown icon)
        - Wait for logout button to appear in dropdown menu
        - Click on logout button

    CHECK:
        - User is redirected to login page
        - Email field is empty
        - Password field is empty
        - Error icons are not visible
    """
    # Perform logout
    with DashboardPage(driver) as dashboard_page:
        # Step 1: Click user dropdown button
        dashboard_page.click_user_dropdown()

        # Step 2: Wait for logout button to appear
        expect(dashboard_page.logout_button).to_be_visible()

        # Step 3: Click logout button
        dashboard_page.click_logout()

        # Wait for page to load after logout
        dashboard_page.page.wait_for_load_state("load")

    # Verify logout successful - check redirect to login page and form state
    with LoginPage(driver) as login_page:
        # Verify we are on login page
        expect(login_page.page).to_have_url(login_page.url, timeout=20000)

        # Wait for login form fields to be visible
        expect(login_page.email_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()

        # Verify form fields are empty
        expect(login_page.email_input).to_have_value("")
        expect(login_page.password_input).to_have_value("")

        # Verify error icons are NOT visible
        expect(login_page.email_error_icon).not_to_be_visible()
        expect(login_page.password_error_icon).not_to_be_visible()
