from playwright.sync_api import expect
from utils.locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        self.page.get_by_placeholder(Locators.USERNAME_INPUT).fill(username)
        self.page.get_by_placeholder(Locators.PASSWORD_INPUT).fill(password)
        self.page.click(Locators.LOGIN_BUTTON) 

    def is_login_successful(self):
       dashboard = self.page.locator("h6:has-text('Dashboard')")
       expect(dashboard).to_be_visible()
       return True

    def get_invalid_credentials_error(self):
        self.page.wait_for_selector(Locators.ERROR_MESSAGE)
        return self.page.text_content(Locators.ERROR_MESSAGE)

    def is_required_field_error_visible(self):
        return self.page.locator(Locators.REQUIRED_FIELD_ERROR).first.is_visible()

    def is_dashboard_visible(self):
        expect(self.page.locator(Locators.DASHBOARD_HEADER)).to_be_visible()
        return True

