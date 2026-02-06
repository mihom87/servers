from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_api_tokens(driver, logged_in_user, identity_and_access_group_clicked):
    """
    Verify that API tokens link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.iam_api_tokens_link).to_be_visible()
        page.side_menu.iam_api_tokens_link.click(trial=True)
        expect(page.side_menu.iam_api_tokens_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/iam/api-tokens"
        )
