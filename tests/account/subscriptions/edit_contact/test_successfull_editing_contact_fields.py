import pytest
from pages.contact_page import ContactPage
from pages.contact_page_edit import ContactPageEdit
from utils.custom_expect import expect

def test_successfull_editing_contact_fields(driver, get_on_edit_contact_page, first_name_edited, last_name_edited, job_title_edited, email_edited, phone_number_edited, secondary_email_edited, comment_edited):
    """
    Verify that user can successfully edit contact fields.

    PRECONDITIONS:
        - User must be logged in
        - User must be on edit contact page
    """
    with ContactPageEdit(driver) as page:
        expect(page.first_name_input).to_be_visible()
        page.fill_first_name(first_name_edited)
        expect(page.last_name_input).to_be_visible()
        page.fill_last_name(last_name_edited)
        expect(page.job_title_input).to_be_visible()
        page.fill_job_title(job_title_edited)
        expect(page.email_input).to_be_visible()
        page.fill_email(email_edited)
        expect(page.phone_number_input).to_be_visible()
        page.fill_phone_number(phone_number_edited)
        expect(page.secondary_email_input).to_be_visible()
        page.fill_secondary_email(secondary_email_edited)
        expect(page.comment_textarea).to_be_visible()
        page.fill_comment(comment_edited)
        expect(page.primary_checkbox).to_be_disabled()
        expect(page.technical_checkbox).to_be_visible()
        page.click_technical_checkbox()
        expect(page.billing_checkbox).to_be_visible()
        page.click_billing_checkbox()
        expect(page.abuse_checkbox).to_be_visible()
        page.click_abuse_checkbox()
        expect(page.emergency_checkbox).to_be_visible()
        expect(page.save_button).to_be_visible()
        page.save_button.click()
        page.page.wait_for_load_state("load")
    with ContactPage(driver) as page:
        expect(page.page).to_have_url(page.path)
        expect(page.first_name_value).to_contain_text(first_name_edited)
        expect(page.last_name_value).to_contain_text(last_name_edited)
        expect(page.job_title_value).to_contain_text(job_title_edited)
        expect(page.email_value).to_contain_text(email_edited)
        expect(page.phone_number_value).to_contain_text(phone_number_edited)
        expect(page.secondary_email_value).to_contain_text(secondary_email_edited)
        expect(page.comments_value).to_contain_text(comment_edited)
        expect(page.role_value).to_contain_text("Emergency")

@pytest.fixture
def first_name_edited():
    return "Test edited"

@pytest.fixture
def last_name_edited():
    return "Contact edited"

@pytest.fixture
def job_title_edited():
    return "QA Engineer edited"

@pytest.fixture
def email_edited():
    return "test.contact.edited@example.com"

@pytest.fixture
def phone_number_edited():
    return "+1234567891"

@pytest.fixture
def secondary_email_edited():
    return "test.contact.secondary.edited@example.com"

@pytest.fixture
def comment_edited():
    return "Test contact comment edited"