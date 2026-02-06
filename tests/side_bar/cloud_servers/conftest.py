from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect
import pytest


@pytest.fixture
def cloud_servers_group_clicked(driver, logged_in_user):
    """
    Verify that cloud servers group is visible in side menu and can be clicked.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.cloud_servers_group).to_be_visible()
        page.side_menu.cloud_servers_group.click()

