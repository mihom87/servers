import pytest
from pages.account_page import AccountPage
from pages.contact_page import ContactPage
from utils.custom_expect import expect
import uuid


def test_successful_delete_contact(
    driver, filled_contact_fields, first_name, last_name
):
    """
    Verify that user can successfully delete contact.

    PRECONDITIONS:
        - User must be logged in
        - User must be on edit contact page
    """
    with AccountPage(driver) as page:
        page.goto()
        expect(page.page).to_have_url(page.url)
        page.page.wait_for_load_state("load")
        expect(page.subscriptions_search_input).to_be_visible()
        page.fill_subscriptions_search_input(first_name)
        contact_row = page.contact_row_by_fullname(f"{first_name} {last_name}")
        expect(contact_row).to_be_visible()
        expect(page.delete_button_in_row(contact_row)).to_be_visible()
        page.click_delete_button_in_row(contact_row)
        expect(page.confirm_delete_dialog).to_be_visible()
        expect(page.confirm_delete_form).to_be_visible()
        expect(page.confirm_delete_button).to_be_visible()
        expect(page.confirm_delete_button).to_be_enabled()
        page.page.wait_for_timeout(500)
        page.click_confirm_delete()
        #
        expect(page.confirm_delete_button).not_to_be_visible()
        expect(page.subscriptions_search_input).to_be_visible()
        page.fill_subscriptions_search_input(first_name)
        expect(contact_row).to_have_count(0)
