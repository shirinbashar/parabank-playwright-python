from playwright.sync_api import Page
from .base_page import BasePage


class AccountOverviewPage(BasePage):
    URL = f"{BasePage.BASE_URL}/parabank/overview.htm"
    HEADING = "Accounts Overview"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # #showError also has an h1.title (hidden); scope to the visible container
        self._heading = page.locator("#showOverview h1.title")
        self._accounts_table = page.locator("#accountTable")
        # Exclude the last row which is the total row
        self._account_rows = page.locator("#accountTable tbody tr:not(:last-child)")

    def navigate(self) -> "AccountOverviewPage":
        self.page.goto(self.URL)
        self.wait_for_load()
        return self

    def is_loaded(self) -> bool:
        self._heading.wait_for(state="visible", timeout=10_000)
        return self.HEADING in self._heading.text_content()

    def get_heading_text(self) -> str:
        self._heading.wait_for(state="visible")
        return self._heading.text_content().strip()

    def get_account_count(self) -> int:
        self._accounts_table.wait_for(state="visible")
        return self._account_rows.count()

    def get_total_balance_text(self) -> str:
        self._accounts_table.wait_for(state="visible")
        # td:nth-child(2) is the balance column; td:last-child is a non-breaking-space placeholder
        total_row = self._accounts_table.locator("tbody tr:last-child td:nth-child(2)")
        total_row.wait_for(state="visible")
        return total_row.text_content().strip()
