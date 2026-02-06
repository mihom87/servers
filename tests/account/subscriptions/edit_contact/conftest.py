import pytest
from pages.contact_page import ContactPage
from pages.contact_page_edit import ContactPageEdit
from utils.custom_expect import expect

@pytest.fixture
def get_on_edit_contact_page(driver, filled_contact_fields):
    with ContactPage(driver) as page:
        page.page.wait_for_load_state("load")
        page.click_edit_button()
    with ContactPageEdit(driver) as page:
        page.page.wait_for_load_state("load")
        expect(page.page).to_have_url(page.path)