from playwright.sync_api import expect
from utils.utility import CommonUtils
from utils.locators import Locators

class Performance:
    def __init__(self, page):
        self.page = page
        self.options = page.locator("div[role='option']")

    def select_from_dropdown(self, locator):
        self.page.locator(locator).click()
        CommonUtils.select_random_option(self.page, self.options)

    def employee_performance(self):
        self.page.get_by_role("link", name=Locators.PERFORMANCE_LINK).click()
        self.page.wait_for_url("**/performance/**", timeout=15000)

        self.page.get_by_placeholder(Locators.EMPLOYEE_NAME_INPUT).fill("a")
        self.options.first.wait_for(state="visible")
        CommonUtils.select_random_option(self.page, self.options)

        self.select_from_dropdown(Locators.JOB_TITLE_DROPDOWN)
        self.select_from_dropdown(Locators.SUBUNIT_DROPDOWN)
        self.select_from_dropdown(Locators.INCLUDE_DROPDOWN)
        self.select_from_dropdown(Locators.REVIEW_STATUS_DROPDOWN)

        self.page.locator(Locators.SEARCH_BUTTON).click()


