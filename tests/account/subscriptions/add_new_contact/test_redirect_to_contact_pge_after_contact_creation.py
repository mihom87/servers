from pages.account_page import AccountPage
from pages.new_contact_page import NewContactPage
from pages.contact_page import ContactPage
from utils.custom_expect import expect


def test_redirect_to_contact_page_after_contact_creation(
    driver, new_contact_page_opened
):
    """
    Verify that user is redirected to contact page after contact creation.

    PRECONDITIONS:
        - User must be logged in
        - User must be on account page
    """
    first_name = "Test"
    last_name = "Contact"
    job_title = "QA Engineer"
    email = "test.contact@example.com"
    phone_number = "+1234567890"
    secondary_email = "test.contact.secondary@example.com"
    comment = "Test contact comment"

    # Fill contact form
    with NewContactPage(driver) as new_contact_page:
        # Wait for form fields to be visible
        expect(new_contact_page.first_name_input).to_be_visible()
        expect(new_contact_page.last_name_input).to_be_visible()

        # Fill all text fields using typing simulation
        new_contact_page.first_name_input.press_sequentially(first_name, delay=50)
        new_contact_page.last_name_input.press_sequentially(last_name, delay=50)
        new_contact_page.job_title_input.press_sequentially(job_title, delay=50)
        new_contact_page.email_input.press_sequentially(email, delay=50)
        new_contact_page.phone_number_input.press_sequentially(phone_number, delay=50)
        new_contact_page.secondary_email_input.press_sequentially(
            secondary_email, delay=50
        )
        new_contact_page.comment_textarea.press_sequentially(comment, delay=50)

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

    # Verify contact was created successfully
    with ContactPage(driver) as contact_page:
        # Verify we are on contact page (URL matches pattern)
        expect(contact_page.page).to_have_url(contact_page.path)
