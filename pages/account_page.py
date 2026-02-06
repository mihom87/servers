from pages.base_page import BasePage
from utils.webdriver import WebDriver
from playwright.sync_api import Locator
from utils.custom_expect import expect


class AccountPage(BasePage):
    """
    Account page class.
    """

    path = "/a:0m5Nx6dn/account"

    def __init__(self, driver: WebDriver):
        """
        Initialize account page.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver, self.__class__.path)

    @property
    def account_link(self) -> Locator:
        """
        Account link in dropdown menu.

        Element a with href to account page, has span in children.
        """
        return self.page.locator(
            '//a[@type="button" and @role="button" and @title="Create"]'
        )

    @property
    def subscriptions_search_input(self):
        return self.page.locator('div:has(h2:has-text("Subscriptions"))').get_by_role("searchbox", name="Search").first
    
    @property
    def confirm_delete_dialog(self):
        return self.page.locator("dialog[open]").filter(has_text="Confirmation")

    @property
    def confirm_delete_form(self):
        return self.confirm_delete_dialog.locator("form")


    @property
    def confirm_delete_button(self) -> Locator:
        dialog = self.page.locator(
        'dialog[open]',
        has=self.page.get_by_role("heading", name="Confirmation")
    )
        return dialog.get_by_role("button", name="Delete")

    
    # Actions
    def click_create_contact(self):
        """Click create account button."""
        self.account_link.click()
    
    def fill_subscriptions_search_input(self, value: str):
        """Fill search input."""
        self.subscriptions_search_input.fill(value)
    
    def contact_row_by_fullname(self, full_name: str) -> Locator:
        return self.page.locator(
            'div:has(h2:has-text("Subscriptions")) tbody tr',
            has=self.page.locator(f'td[data-label="Name"] span[title="{full_name}"]'),
        )
    
    def delete_button_in_row(self, row: Locator) -> Locator:
     return row.locator('td:last-child button')
    
    def click_delete_button_in_row(self, row: Locator):
        self.delete_button_in_row(row).click()
    
    def click_confirm_delete(self):
        with self.page.expect_response(
        lambda r: r.request.method == "DELETE" and "/rest/contacts/" in r.url
    ):
            self.confirm_delete_button.click(delay=2000)
        

    # def click_confirm_delete(self):
    # # блокируем только "нативный submit" (POST как document navigation)
    #     delete_dialog = self.page.locator("dialog[open]").filter(has=self.page.get_by_role("heading", name="Confirmation"))
    #     def block_bad_submit(route):
            
    #         req = route.request
    #         if req.method == "POST" and req.resource_type == "document":
    #             route.abort()
    #         else:
    #             route.continue_()

        
    #     self.page.route("**/*", block_bad_submit)
    #     try:
    #         expect(delete_dialog).to_be_visible()
    #         expect(self.confirm_delete_button).to_be_visible()
    #         expect(self.confirm_delete_button).to_be_enabled()

    #         self.confirm_delete_button.click(no_wait_after=True)
    #         expect(delete_dialog).to_be_hidden()  # модалка закрылась
    #     finally:
    #         self.page.unroute("**/*", block_bad_submit)

    
