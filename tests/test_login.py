"""
Test for login functionality.

Test file: test_login.py
Test name: test_login
"""

import pytest
from pages.main_page import MainPage
from utils.custom_expect import expect


def test_login(driver):
    """
    Test login flow on servers.com main page.

    Steps:
        1. Open main page
        2. Verify page is loaded
        3. Click on Customer portal button
        4. Verify navigation to login page

    Args:
        driver: WebDriver fixture from conftest.py
    """
    # Step 1: Open main page
    main_page = MainPage(driver)
    main_page.goto()

    