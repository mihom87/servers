"""
Fixtures for login tests.
"""

import pytest
from pages.login_page import LoginPage
from utils.custom_expect import expect


@pytest.fixture
def opened_login_page(driver):
    """
    Open login page and wait for form fields to be visible.

    This fixture modifies driver state by opening the login page
    and waiting for fields. Tests can then create their own LoginPage
    instance with the same driver to interact with the already-opened page.

    Args:
        driver: WebDriver fixture from conftest.py
    """
    with LoginPage(driver) as login_page:
        login_page.goto()

        # Wait for login form fields to be visible
        expect(login_page.email_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()
