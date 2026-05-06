import pytest
from pages.login_page import LoginPage



def test_login_positive(page):
    login = LoginPage(page)
    
    login.login("Admin", "admin123")
    assert login.is_login_successful()

    assert login.is_dashboard_visible()
