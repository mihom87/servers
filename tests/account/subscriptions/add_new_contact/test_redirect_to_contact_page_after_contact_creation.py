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
    with NewContactPage(driver) as page:
        # Wait for form fields to be visible
        expect(page.first_name_input).to_be_visible()
        expect(page.last_name_input).to_be_visible()
        expect(page.job_title_input).to_be_visible()
        expect(page.email_input).to_be_visible()
        expect(page.phone_number_input).to_be_visible()
        expect(page.secondary_email_input).to_be_visible()
        expect(page.comment_textarea).to_be_visible()
        expect(page.primary_checkbox).to_be_visible()
        expect(page.technical_checkbox).to_be_visible()
        expect(page.billing_checkbox).to_be_visible()
        expect(page.abuse_checkbox).to_be_visible()
        expect(page.emergency_checkbox).to_be_visible()

        # Fill all text fields using typing simulation
        page.first_name_input.press_sequentially(first_name, delay=50)
        page.last_name_input.press_sequentially(last_name, delay=50)
        page.job_title_input.press_sequentially(job_title, delay=50)
        page.email_input.press_sequentially(email, delay=50)
        page.phone_number_input.press_sequentially(phone_number, delay=50)
        page.secondary_email_input.press_sequentially(
            secondary_email, delay=50
        )
        page.comment_textarea.press_sequentially(comment, delay=50)

        # Check all checkboxes
        # new_contact_page.click_primary_checkbox()
        page.click_technical_checkbox()
        page.click_billing_checkbox()
        page.click_abuse_checkbox()
        page.click_emergency_checkbox()

        # Click create button
        page.create_button.click()

        # Wait for page to fully load after contact creation
        page.page.wait_for_load_state("load")

    # Verify contact was created successfully
    with ContactPage(driver) as page:
        # Verify we are on contact page (URL matches pattern)
        expect(page.page).to_have_url(page.path)
