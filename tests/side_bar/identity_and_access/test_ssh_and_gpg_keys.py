from pages.dashboard_page import DashboardPage
from utils.custom_expect import expect


def test_ssh_and_gpg_keys(driver, logged_in_user, identity_and_access_group_clicked):
    """
    Verify that SSH and GPG keys link is visible in side menu and leads to the correct page.
    """
    with DashboardPage(driver) as page:
        expect(page.side_menu.iam_ssh_gpg_keys_link).to_be_visible()
        page.side_menu.iam_ssh_gpg_keys_link.click(trial=True)
        expect(page.side_menu.iam_ssh_gpg_keys_link).to_have_attribute(
            "href", "/a:0m5Nx6dn/iam/keys"
        )
