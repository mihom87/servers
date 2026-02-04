from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_unsuccessful_login_with_empty_password(driver, opened_login_page):
    """
    Verify that login fails when password field is empty.

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page

    ACTION:
        - Enter valid email address in the email field
        - Leave password field empty
        - Click on Login button

    CHECK:
        - Login is not successful
        - Error message is displayed indicating that password field is required
        - User remains on the login page
    """
    with LoginPage(driver) as login_page:
        # Fill email, leave password field empty
        login_page.fill_email("day+test9@servers.com")

        # Click login button
        login_page.click_login()

        # Wait for page to process
        login_page.page.wait_for_load_state("load")

        # Verify we are still on login page
        expect(login_page.page).to_have_url(login_page.url)

        # Verify error icon appears for password field
        expect(login_page.password_error_icon).to_be_visible()
