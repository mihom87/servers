from pages.dashboard_page import DashboardPage
from pages.account_page import AccountPage
from utils.custom_expect import expect


def test_create_and_manage(driver, logged_in_user, cloud_servers_group_clicked):
    """
    Verify that create and manage link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.cloud_create_manage_link).to_be_visible()
        page.side_menu.cloud_create_manage_link.click(trial=True)
        expect(page.side_menu.cloud_create_manage_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/cloud-computing?page=1"
        )
