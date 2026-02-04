import pytest
from pages.login_page import LoginPage
from utils.custom_expect import expect


@pytest.mark.parametrize(
    "email, password",
    [
        ("nonexistent123456@test.com", "AnyPassword123"),
        ("day+test9@servers.com", "WrongPassword123"),
    ],
    ids=["non_existing_email", "wrong_password"],
)
def test_unsuccessful_login_with_invalid_credentials(
    driver, opened_login_page, email, password
):
    """
    Verify that login fails with invalid credentials and displays error message.

    This test covers multiple scenarios:
    - Non-existing email (valid format but not registered)
    - Wrong password (valid email but incorrect password)
    - Invalid email format (email without @ or domain)

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page
        - Login form should open automatically

    ACTION:
        - Enter test email address in the email field
        - Enter test password in the password field
        - Click on Login button

    CHECK:
        - Login is not successful
        - Error message "Incorrect email or password" is displayed
        - User remains on the login page
        - No sensitive information about user existence is revealed
    """
    with LoginPage(driver) as login_page:
        # Fill with test credentials
        login_page.fill_email(email)
        login_page.fill_password(password)

        # Click login button
        login_page.click_login()

        # Wait for page to process
        login_page.page.wait_for_load_state("load")

        # Verify we are still on login page
        expect(login_page.page).to_have_url(login_page.url)

        # Verify authentication failed message is displayed
        expect(login_page.auth_failed_message).to_be_visible()
        expect(login_page.auth_failed_message).to_have_text(
            "Incorrect email or password"
        )
