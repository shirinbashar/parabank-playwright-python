import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestValidLogin:
    @pytest.mark.smoke
    def test_valid_login_shows_logout_link(self, login_page: LoginPage):
        login_page.login("john", "demo")
        home = HomePage(login_page.page)
        assert home.is_logged_in(), "Log Out link must appear after successful login"

    @pytest.mark.smoke
    def test_valid_login_leaves_login_page(self, login_page: LoginPage):
        login_page.login("john", "demo")
        assert "index.htm" not in login_page.get_current_url()


class TestInvalidLogin:
    @pytest.mark.negative
    def test_wrong_credentials_show_error(self, login_page: LoginPage):
        login_page.login("invalid_user", "wrong_pass")
        error = login_page.get_error_message()
        assert "could not be verified" in error.lower(), (
            f"Expected verification-error message, got: {error!r}"
        )

    @pytest.mark.negative
    def test_empty_credentials_show_error(self, login_page: LoginPage):
        login_page.login("", "")
        assert login_page.is_error_displayed(), (
            "An error message must be displayed when credentials are empty"
        )

    @pytest.mark.negative
    def test_valid_user_wrong_password_shows_error(self, login_page: LoginPage):
        login_page.login("john", "wrong_password")
        error = login_page.get_error_message()
        assert error, "Error message should not be empty for wrong password"
