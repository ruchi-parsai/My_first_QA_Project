from pages.login_page import LoginPage
from pages.performance_page import Performance


def test_performance_flow(page):
    login = LoginPage(page)
    login.login("Admin", "admin123")

    performance = Performance(page)
    performance.employee_performance()