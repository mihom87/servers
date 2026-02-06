import pytest
from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


@pytest.fixture
def enterprise_bare_metal_group_clicked(driver):
    with DashboardPage(driver) as page:
        expect(page.side_menu.enterprise_bare_metal_group).to_be_visible()
        page.side_menu.enterprise_bare_metal_group.click()