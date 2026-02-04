import pytest
from pages.account_page import AccountPage
from pages.new_contact_page import NewContactPage
from pages.contact_page import ContactPage
from utils.custom_expect import expect


def test_new_contact_page_opened(driver, account_page_opened):
    """
    Verify that user is redirected to new contact page after clicking create contact button.

    PRECONDITIONS:
        - User must be logged in
        - User must be on account page
    ACTION:
        - Click create contact button
    CHECK:
        - User is redirected to new contact page
        - New contact page is opened
        - All form fields are visible
    """
    with AccountPage(driver) as account_page:
        # Click create contact button
        account_page.click_create_contact()

        # Wait for page to load
        account_page.page.wait_for_load_state("load")


    with NewContactPage(driver) as new_contact_page:
        # Verify we are on new contact page (URL matches pattern)

        expect(new_contact_page.page).to_have_url(new_contact_page.url)

        # Verify all form fields are visible
        expect(new_contact_page.first_name_input).to_be_visible()
        expect(new_contact_page.last_name_input).to_be_visible()
        expect(new_contact_page.job_title_input).to_be_visible()
        expect(new_contact_page.email_input).to_be_visible()
        expect(new_contact_page.phone_number_input).to_be_visible()
        expect(new_contact_page.secondary_email_input).to_be_visible()
        expect(new_contact_page.comment_textarea).to_be_visible()