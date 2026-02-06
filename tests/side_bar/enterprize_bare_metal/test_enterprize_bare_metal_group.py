import pytest
from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect



def test_enterprise_bare_metal_group_clicked(driver, logged_in_user):
    """
    Verify that enterprise bare metal group is visible in side menu and can be clicked.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.enterprise_bare_metal_group).to_be_visible()
        page.side_menu.enterprise_bare_metal_group.click()
