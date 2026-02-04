from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_unsuccessful_login_with_both_fields_empty(driver, opened_login_page):
    """
    Verify that login fails when both email and password fields are empty.

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page

    ACTION:
        - Leave email field empty
        - Leave password field empty
        - Click on Login button

    CHECK:
        - Login is not successful
        - Error messages are displayed for both email and password fields
        - User remains on the login page
        - Login button may be disabled until fields are filled
    """
    with LoginPage(driver) as login_page:
        # Leave both fields empty - do not fill them

        # Click login button
        login_page.click_login()

        # Wait for page to process
        login_page.page.wait_for_load_state("load")

        # Verify we are still on login page
        expect(login_page.page).to_have_url(login_page.url)

        # Verify error icons appear for both fields
        expect(login_page.email_error_icon).to_be_visible()
        expect(login_page.password_error_icon).to_be_visible()
