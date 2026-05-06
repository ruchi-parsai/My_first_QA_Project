class Locators:
    # login_page
    USERNAME_INPUT = "Username"
    PASSWORD_INPUT = "Password"
    LOGIN_BUTTON = 'button[type="submit"]'
    ERROR_MESSAGE = ".oxd-alert-content-text"
    REQUIRED_FIELD_ERROR = ".oxd-input-group__message"
    DASHBOARD_HEADER = "h6.oxd-text--h6"       
    

    # performance_page
    PERFORMANCE_LINK = "Performance"
    EMPLOYEE_NAME_INPUT =  "Type for hints..."

    JOB_TITLE_DROPDOWN = '(//div[@class="oxd-select-text--after"]/i[contains(@class, "oxd-icon bi-caret-down-fill")])[1]'
    JOB_TITLE_OPTION =  "//div[@role='option']//span[text()='QA Engineer']"
    SUBUNIT_DROPDOWN =  '(//div[@class="oxd-select-text--after"]/i[contains(@class, "oxd-icon bi-caret-down-fill")])[2]'
    SUBUNIT_OPTION = "//div[@role='option']//span[text()='Sales']"
    OPTIONS = "div[role='option']"
    INCLUDE_DROPDOWN = '(//div[@class="oxd-select-text--after"]/i[contains(@class, "oxd-icon bi-caret-down-fill")])[3]'
    REVIEW_STATUS_DROPDOWN = '(//div[@class="oxd-select-text--after"]/i[contains(@class, "oxd-icon bi-caret-down-fill")])[4]'
    SEARCH_BUTTON =  "//button[@type='submit']"


    #recruitment_page
    RECRUITMENT_OPTION = "Recruitment"
    JOB_TITLE_DROPDOWN_2= "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[1]"
    VACANCY_DROPDOWN = "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[2]"
    HIRING_MANAGER_DROPDOWN = "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[3]"
    STATUS_DROPDOWN = "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[4]"
    # JOB_TITLE_OPTION = "option", name="HR Manager"
    DATE_FROM = '//input[@placeholder="From" and @class="oxd-input oxd-input--active"]'
    DATE_TO = '//input[@placeholder="To" and @class="oxd-input oxd-input--active"]'
    SEARCH_BUTTON = '//button[@type="submit"]'
    RESULTS_TABLE = "div.oxd-table-body"
    ADD_BUTTON = '//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--secondary"]'
    FIRST_NAME = '//input[@placeholder="First Name"]'
    MIDDLE_NAME = '//input[@placeholder="Middle Name"]'
    LAST_NAME = '//input[@placeholder="Last Name"]'
    VACANCY_DROPDOWN_1 = "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[1]"
    EMAIL_INPUT = '(//input[@placeholder="Type here"])[1]'
    CONTACT_NUMBER_INPUT = '(//input[@placeholder="Type here"])[2]'
    SAVE_BUTTON = '//button[@type="submit" and @class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    SUCCESS_POPUP = '//p[text()="Successfully Saved"]'
    SHORTLIST_BUTTON = '//button[normalize-space()="Shortlist"]'
    OPTIONS = "div[role='option']"