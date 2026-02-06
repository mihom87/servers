from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_reports_cloud_servers(driver, logged_in_user, reports_group_clicked):
    """
    Verify that reports cloud servers link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.reports_cloud_servers_link).to_be_visible()
        page.side_menu.reports_cloud_servers_link.click(trial=True)
        expect(page.side_menu.reports_cloud_servers_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/cloud-computing/reports?fs=0"
        )
