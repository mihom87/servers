import pytest
from pages.new_contact_page import NewContactPage
from pages.contact_page import ContactPage
from utils.custom_expect import expect


def test_contact_fields_filled_correctly_after_contact_creation(
    driver,
    filled_contact_fields,
    first_name,
    last_name,
    job_title,
    email,
    phone_number,
    secondary_email,
    comment,
):
    """
    Verify that contact fields are filled correctly after contact creation.

    PRECONDITIONS:
        - User must be logged in
        - User must be on new contact page
    """
    with ContactPage(driver) as contact_page:
        # Verify we are on contact page (URL matches pattern)
        expect(contact_page.page).to_have_url(contact_page.path)

        # Verify all filled fields have correct values
        expect(contact_page.first_name_value).to_contain_text(first_name)
        expect(contact_page.last_name_value).to_contain_text(last_name)
        expect(contact_page.job_title_value).to_contain_text(job_title)
        expect(contact_page.email_value).to_contain_text(email)
        expect(contact_page.phone_number_value).to_contain_text(phone_number)
        expect(contact_page.secondary_email_value).to_contain_text(secondary_email)
        expect(contact_page.comments_value).to_contain_text(comment)
        expect(contact_page.role_value).to_contain_text("Technical")
        expect(contact_page.role_value).to_contain_text("Billing")
        expect(contact_page.role_value).to_contain_text("Abuse")
        expect(contact_page.role_value).to_contain_text("Emergency")
