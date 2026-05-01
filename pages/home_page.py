from playwright.sync_api import Page
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._logout_link = page.locator('a[href*="logout"]')
        self._account_overview_link = page.locator('a[href*="overview"]')
        self._welcome_text = page.locator("#leftPanel p.smallText")

    def is_logged_in(self) -> bool:
        self._logout_link.wait_for(state="visible", timeout=10_000)
        return self._logout_link.is_visible()

    def get_welcome_text(self) -> str:
        self._welcome_text.wait_for(state="visible")
        return self._welcome_text.text_content().strip()

    def go_to_account_overview(self) -> None:
        self._account_overview_link.first.click()
        self.wait_for_load()

    def logout(self) -> None:
        self._logout_link.click()
        self.wait_for_load()
