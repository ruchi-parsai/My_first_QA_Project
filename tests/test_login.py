import pytest
from pages.login_page import LoginPage



def test_login_positive(page):
    login = LoginPage(page)
    
    login.login("Admin", "admin123")
    assert login.is_login_successful()

    assert login.is_dashboard_visible()

# @pytest.mark.parametrize(
#     "username,password,scenario",
#     [
#         ("WrongUser", "admin123", "invalid"),
#         ("Admin", "wrongpass", "invalid"),
#         ("Wrong", "wrong", "invalid"),
#         ("", "", "empty"),
#     ]
# )
# def test_login_negative(page, username, password, scenario):
#     login = LoginPage(page)
#     login.login(username, password)

#     if scenario == "invalid":
#         assert "Invalid credentials" in login.get_invalid_credentials_error()

#     elif scenario == "empty":
#         assert login.is_required_field_error_visible()