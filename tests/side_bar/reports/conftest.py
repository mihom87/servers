from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect
import pytest


@pytest.fixture
def reports_group_clicked(driver, logged_in_user):
    """
    Verify that reports group is visible in side menu and can be clicked.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.reports_group).to_be_visible()
        page.side_menu.reports_group.click()
