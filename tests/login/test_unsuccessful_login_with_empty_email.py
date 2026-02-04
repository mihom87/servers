from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_unsuccessful_login_with_empty_email(driver, opened_login_page):
    """
    Verify that login fails when email field is empty.

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page
        - Login form should open automatically

    ACTION:
        - Leave email field empty
        - Enter valid password in the password field
        - Click on Login button

    CHECK:
        - Login is not successful
        - Error message is displayed indicating that email field is required
        - User remains on the login page
    """
    with LoginPage(driver) as login_page:
        # Leave email field empty, fill password
        login_page.fill_password("Twz8pyE5B9Y3")

        # Click login button
        login_page.click_login()

        # Wait for page to process
        login_page.page.wait_for_load_state("load")

        # Verify we are still on login page
        expect(login_page.page).to_have_url(login_page.url)

        # Verify error icon appears for email field
        expect(login_page.email_error_icon).to_be_visible()
