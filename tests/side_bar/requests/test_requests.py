from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_requests(driver, logged_in_user):
    """
    Verify that requests link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.requests_link).to_be_visible()
        page.side_menu.requests_link.click(trial=True)
        expect(page.side_menu.requests_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/requests"
        )
