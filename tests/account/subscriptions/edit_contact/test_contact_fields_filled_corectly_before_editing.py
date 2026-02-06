import pytest
from pages.new_contact_page import NewContactPage
from pages.contact_page import ContactPage
from pages.contact_page_edit import ContactPageEdit
from utils.custom_expect import expect


def test_contact_fields_filled_corectly_before_editing(driver, filled_contact_fields, first_name, last_name, job_title, email, phone_number, secondary_email, comment):
    """
    Verify that contact fields are filled correctly before editing.

    PRECONDITIONS:
        - User must be logged in
        - User must be on contact page
    """
    with ContactPage(driver) as page:
        # Verify we are on contact page (URL matches pattern)
        expect(page.page).to_have_url(page.path)
        page.click_edit_button()
    
    with ContactPageEdit(driver) as page:
        page.page.wait_for_load_state("load")
        expect(page.page).to_have_url(page.path)
        # Verify we are on contact page edit (URL matches pattern)
        expect(page.page).to_have_url(page.path)
        expect(page.first_name_input).to_have_value(first_name)
        expect(page.last_name_input).to_have_value(last_name)
        expect(page.job_title_input).to_have_value(job_title)
        expect(page.email_input).to_have_value(email)
        expect(page.phone_number_input).to_have_value(phone_number)
        expect(page.secondary_email_input).to_have_value(secondary_email)
        expect(page.comment_textarea).to_have_value(comment)
        expect(page.primary_checkbox).not_to_be_checked()
        expect(page.technical_checkbox).to_be_checked()
        expect(page.billing_checkbox).to_be_checked()
        expect(page.abuse_checkbox).to_be_checked()
        expect(page.emergency_checkbox).to_be_checked()
