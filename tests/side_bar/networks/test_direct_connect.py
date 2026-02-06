from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_direct_connect(driver, logged_in_user, networks_group_clicked):
    """
    Verify that direct connect link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.networks_direct_connect_link).to_be_visible()
        page.side_menu.networks_direct_connect_link.click(trial=True)
        expect(page.side_menu.networks_direct_connect_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/networks/dc"
        )
