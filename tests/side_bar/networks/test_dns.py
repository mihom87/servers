from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_dns(driver, logged_in_user, networks_group_clicked):
    """
    Verify that DNS link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.networks_dns_link).to_be_visible()
        page.side_menu.networks_dns_link.click(trial=True)
        expect(page.side_menu.networks_dns_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/networks/dns"
        )
