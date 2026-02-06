import pytest
from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


@pytest.fixture
def monitoring_group_clicked(driver):
    with DashboardPage(driver) as page:
        expect(page.side_menu.monitoring_text_item).to_be_visible()
        page.side_menu.monitoring_text_item.click()
