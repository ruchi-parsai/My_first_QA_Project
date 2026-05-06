from pages.login_page import LoginPage
from pages.recruitment_page import Recruitment

def test_recruitment_flow(page):
    login = LoginPage(page)
    login.login("Admin", "admin123")

    recruitment = Recruitment(page)
    recruitment.employee_recruitment()
    recruitment.add()