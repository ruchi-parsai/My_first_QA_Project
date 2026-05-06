from playwright.sync_api import expect
from utils.testdata import TestData
from utils.utility import CommonUtils
from utils.locators import Locators


class Recruitment:
    def __init__(self, page):
        self.page = page
        self.data = TestData()
        self.options = page.locator("div[role='option']")

    def select_from_dropdown(self, locator):
        self.page.locator(locator).click()
        CommonUtils.select_random_option(self.page, self.options)
    

    def employee_recruitment(self):
        self.page.get_by_role("link", name=Locators.RECRUITMENT_OPTION).click()
        self.select_from_dropdown(Locators.JOB_TITLE_DROPDOWN_2)
        self.select_from_dropdown(Locators.VACANCY_DROPDOWN)
        self.select_from_dropdown(Locators.HIRING_MANAGER_DROPDOWN)
        self.select_from_dropdown(Locators.STATUS_DROPDOWN)

        start_date = self.data.date_1()
        end_date = self.data.date_2()

        self.page.locator(Locators.DATE_FROM).fill(start_date)
        self.page.locator(Locators.DATE_TO).fill(end_date)

        expect(self.page.locator(Locators.RESULTS_TABLE)).to_be_visible(timeout=10000)
        self.page.locator(Locators.RESULTS_TABLE).scroll_into_view_if_needed()
        self.page.locator(Locators.ADD_BUTTON).scroll_into_view_if_needed()

    def add(self):
        self.page.locator(Locators.ADD_BUTTON).click() 
        fname = self.data.get_first_name()
        self.page.locator(Locators.FIRST_NAME).fill(fname)

        lname =self.data.get_last_name()
        self.page.locator(Locators.LAST_NAME).fill(lname)

        self.select_from_dropdown(Locators.VACANCY_DROPDOWN_1)

        email=self.data.get_email()
        self.page.locator(Locators.EMAIL_INPUT).fill(email)

        number=self.data.get_phone()
        self.page.locator(Locators.CONTACT_NUMBER_INPUT).fill(number)

 
        self.page.locator(Locators.SAVE_BUTTON).scroll_into_view_if_needed()
        self.page.locator(Locators.SAVE_BUTTON).click()

        expect(self.page.locator(Locators.SUCCESS_POPUP)).to_be_visible(timeout=10000)
        message = self.page.locator(Locators.SUCCESS_POPUP).inner_text().strip()
        print(f"Success Message: {message}")

        expect(self.page.locator(Locators.SUCCESS_POPUP)).to_contain_text("Successfully Saved")
        
        # self.page.wait_for_load_state("networkidle")
        # expect(self.shortlist_button).to_be_visible(timeout=10000)
        # self.shortlist_button.click()







        # expect(self.save_button).to_be_visible(timeout=10000)
        # self.save_button.click()