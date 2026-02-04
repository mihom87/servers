from pages.login_page import LoginPage
from utils.custom_expect import expect


def test_error_icons_not_visible_initially(driver, opened_login_page):
    """
    Verify that error icons are not displayed on clean login form.

    This test ensures that validation errors appear only after user interaction
    (e.g., form submission), not automatically on page load. This is correct UX behavior.

    PRECONDITIONS:
        - User must be logged out
        - Navigate to the main page
        - Login form should open automatically

    ACTION:
        - Navigate to login page
        - Wait for form fields to be visible

    CHECK:
        - Email error icon is NOT visible
        - Password error icon is NOT visible
        - Form is in clean initial state without validation errors
    """
    with LoginPage(driver) as login_page:
        # Navigate to login page
        login_page.goto()

        # Wait for login form fields to be visible
        expect(login_page.email_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()

        # Verify error icons are NOT visible on initial load
        expect(login_page.email_error_icon).not_to_be_visible()
        expect(login_page.password_error_icon).not_to_be_visible()
