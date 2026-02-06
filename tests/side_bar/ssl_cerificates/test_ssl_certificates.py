from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_ssl_certificates(driver, logged_in_user):
    """
    Verify that SSL certificates link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.ssl_certificates_link).to_be_visible()
        page.side_menu.ssl_certificates_link.click(trial=True)
        expect(page.side_menu.ssl_certificates_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/ssl"
        )
