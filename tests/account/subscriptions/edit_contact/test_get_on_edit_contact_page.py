from pages.contact_page import ContactPage
from utils.custom_expect import expect


def test_get_on_edit_contact_page(driver, filled_contact_fields):
    """
    Verify that user can get on edit contact page.

    PRECONDITIONS:
        - User must be logged in
        - User must be on contact page
    """
    with ContactPage(driver) as page:
        page.click_edit_button()
        page.page.wait_for_load_state("load")
        expect(page.page).to_have_url(page.path)