"""
Fixtures for account tests.
"""

import pytest
from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from utils.custom_expect import expect


@pytest.fixture
def account_page_opened(driver, logged_in_user):
    """
    Open account page from dashboard.

    This fixture performs login and navigates to account page.
    After this fixture, user is on account page ready for account tests.

    Args:
        driver: WebDriver fixture from conftest.py
        logged_in_user: Fixture that logs in user first
    """
    # Open dropdown menu and navigate to account page
    with DashboardPage(driver) as dashboard_page:
        # Click user dropdown button to open menu
        dashboard_page.click_user_dropdown()

        # Wait for account button to appear
        expect(dashboard_page.account_link).to_be_visible()

        # Click account button
        dashboard_page.click_account()

        # Wait for page to load
        dashboard_page.page.wait_for_load_state("load")

    # Verify we are on account page
    with AccountPage(driver) as account_page:
        # Verify we are on account page
        expect(account_page.page).to_have_url(account_page.url)
