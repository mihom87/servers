import pytest
from pages.account_page import AccountPage
from pages.new_contact_page import NewContactPage
from pages.contact_page import ContactPage
from utils.custom_expect import expect


@pytest.fixture
def new_contact_page_opened(driver, account_page_opened):
    # Navigate to new contact page
    with AccountPage(driver) as account_page:
        # Click create contact button
        account_page.click_create_contact()

        # Wait for page to load
        account_page.page.wait_for_load_state("load")

@pytest.fixture
def filled_contact_fields(driver, new_contact_page_opened, first_name, last_name, job_title, email, phone_number, secondary_email, comment):
    """
    Fill contact fields with test data.

    PRECONDITIONS:
        - User must be logged in
        - User must be on new contact page
    """

    # Fill contact form
    with NewContactPage(driver) as new_contact_page:
        # Wait for form fields to be visible
        expect(new_contact_page.first_name_input).to_be_visible()
        expect(new_contact_page.last_name_input).to_be_visible()

        # Fill all text fields using typing simulation
        new_contact_page.first_name_input.press_sequentially(first_name, delay=50)
        new_contact_page.last_name_input.press_sequentially(last_name, delay=50)
        new_contact_page.job_title_input.press_sequentially(job_title, delay=50)
        new_contact_page.email_input.press_sequentially(
            email, delay=50
        )
        new_contact_page.phone_number_input.press_sequentially(phone_number, delay=50)
        new_contact_page.secondary_email_input.press_sequentially(
            secondary_email, delay=50
        )
        new_contact_page.comment_textarea.press_sequentially(
            comment, delay=50
        )

        # Check all checkboxes
        # new_contact_page.click_primary_checkbox()
        new_contact_page.click_technical_checkbox()
        new_contact_page.click_billing_checkbox()
        new_contact_page.click_abuse_checkbox()
        new_contact_page.click_emergency_checkbox()

        # Click create button
        new_contact_page.create_button.click()

        # Wait for page to fully load after contact creation
        new_contact_page.page.wait_for_load_state("load")



@pytest.fixture
def first_name():
    return "Test"

@pytest.fixture
def last_name():
    return "Contact"

@pytest.fixture
def job_title():
    return "QA Engineer"

@pytest.fixture
def email():
    return "test.contact@example.com"

@pytest.fixture
def phone_number():
    return "+1234567890"

@pytest.fixture
def secondary_email():
    return "test.contact.secondary@example.com"

@pytest.fixture
def comment():
    return "Test contact comment"