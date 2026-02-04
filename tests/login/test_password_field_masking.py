from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_password_field_masking(driver, opened_login_page):
    """
    Verify that password field masks entered characters for security.

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page
        - Login form should open automatically

    ACTION:
        - Navigate to login page
        - Wait for password field to be visible

    CHECK:
        - Password field has type="password" attribute
        - This ensures browser will mask characters (displayed as dots or asterisks)
    """
    with LoginPage(driver) as login_page:
        # Verify password field has correct type for masking
        expect(login_page.password_input).to_have_attribute("type", "password")
