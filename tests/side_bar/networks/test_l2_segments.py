from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_l2_segments(driver, logged_in_user, networks_group_clicked):
    """
    Verify that L2 segments link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.networks_l2_segments_link).to_be_visible()
        page.side_menu.networks_l2_segments_link.click(trial=True)
        expect(page.side_menu.networks_l2_segments_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/networks/l2"
        )
