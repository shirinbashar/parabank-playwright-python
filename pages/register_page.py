from playwright.sync_api import Page
from .base_page import BasePage


class RegisterPage(BasePage):
    URL = f"{BasePage.BASE_URL}/parabank/register.htm"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._first_name = page.locator('input[id="customer.firstName"]')
        self._last_name = page.locator('input[id="customer.lastName"]')
        self._address = page.locator('input[id="customer.address.street"]')
        self._city = page.locator('input[id="customer.address.city"]')
        self._state = page.locator('input[id="customer.address.state"]')
        self._zip_code = page.locator('input[id="customer.address.zipCode"]')
        self._phone = page.locator('input[id="customer.phoneNumber"]')
        self._ssn = page.locator('input[id="customer.ssn"]')
        self._username = page.locator('input[id="customer.username"]')
        self._password = page.locator('input[id="customer.password"]')
        self._confirm_password = page.locator('input[id="repeatedPassword"]')
        self._register_btn = page.locator('input[value="Register"]')
        self._page_heading = page.locator("h1.title")
        self._errors = page.locator(".error")

    def navigate(self) -> "RegisterPage":
        self.page.goto(self.URL)
        self.wait_for_load()
        return self

    def register(self, user_data: dict) -> None:
        self._first_name.fill(user_data["first_name"])
        self._last_name.fill(user_data["last_name"])
        self._address.fill(user_data["address"])
        self._city.fill(user_data["city"])
        self._state.fill(user_data["state"])
        self._zip_code.fill(user_data["zip_code"])
        self._phone.fill(user_data["phone"])
        self._ssn.fill(user_data["ssn"])
        self._username.fill(user_data["username"])
        self._password.fill(user_data["password"])
        self._confirm_password.fill(user_data["confirm_password"])
        self._register_btn.click()

    def is_registered_successfully(self) -> bool:
        self._page_heading.wait_for(state="visible", timeout=10_000)
        return "Welcome" in self._page_heading.text_content()

    def get_heading_text(self) -> str:
        self._page_heading.wait_for(state="visible")
        return self._page_heading.text_content().strip()

    def get_error_messages(self) -> list[str]:
        self._errors.first.wait_for(state="visible", timeout=5_000)
        return [el.text_content().strip() for el in self._errors.all()]
