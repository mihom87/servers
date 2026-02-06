from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect

def test_manage_link(driver, logged_in_user, enterprise_bare_metal_group_clicked):
    """
    Verify that manage link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.ebm_manage_link).to_be_visible()
        page.side_menu.ebm_manage_link.click(trial=True)
        expect(page.side_menu.ebm_manage_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/servers/my"
        )