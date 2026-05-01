import pytest
from playwright.sync_api import Page

from pages.account_overview_page import AccountOverviewPage
from pages.home_page import HomePage


class TestAccountOverview:
    @pytest.mark.smoke
    def test_overview_page_loads_after_login(self, authenticated_page: Page):
        overview = AccountOverviewPage(authenticated_page)
        overview.navigate()
        assert overview.is_loaded(), (
            f"Expected heading '{AccountOverviewPage.HEADING}', "
            f"got: {overview.get_heading_text()!r}"
        )

    @pytest.mark.smoke
    def test_overview_shows_at_least_one_account(self, authenticated_page: Page):
        overview = AccountOverviewPage(authenticated_page)
        overview.navigate()
        count = overview.get_account_count()
        assert count > 0, "At least one account row must be visible in the overview table"

    @pytest.mark.regression
    def test_overview_accessible_via_left_nav(self, authenticated_page: Page):
        home = HomePage(authenticated_page)
        home.go_to_account_overview()
        overview = AccountOverviewPage(authenticated_page)
        assert overview.is_loaded(), "Account Overview must load when navigated via the left nav"

    @pytest.mark.regression
    def test_overview_total_balance_is_displayed(self, authenticated_page: Page):
        overview = AccountOverviewPage(authenticated_page)
        overview.navigate()
        total = overview.get_total_balance_text()
        assert total, "Total balance text must be present in the last row"
