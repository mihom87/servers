from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_volumes(driver, logged_in_user, cloud_servers_group_clicked):
    """
    Verify that volumes link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.cloud_volumes_link).to_be_visible()
        page.side_menu.cloud_volumes_link.click(trial=True)
        expect(page.side_menu.cloud_volumes_link).to_have_attribute(
            "href",
            "/a:0m5Nx6dn/cloud-computing/block-storage",
        )
