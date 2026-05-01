from playwright.sync_api import Page
from .base_page import BasePage


class LoginPage(BasePage):
    URL = f"{BasePage.BASE_URL}/parabank/index.htm"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._username_input = page.locator('input[name="username"]')
        self._password_input = page.locator('input[name="password"]')
        self._login_btn = page.locator('input[value="Log In"]')
        self._error_msg = page.locator("p.error")

    def navigate(self) -> "LoginPage":
        self.page.goto(self.URL)
        self.wait_for_load()
        return self

    def login(self, username: str, password: str) -> None:
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_btn.click()

    def get_error_message(self) -> str:
        self._error_msg.wait_for(state="visible")
        return self._error_msg.text_content().strip()

    def is_error_displayed(self) -> bool:
        try:
            self._error_msg.wait_for(state="visible", timeout=5_000)
            return True
        except Exception:
            return False
