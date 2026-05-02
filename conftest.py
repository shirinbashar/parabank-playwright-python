import pytest
from playwright.sync_api import Page, Playwright, APIRequestContext

from pages.login_page import LoginPage

VALID_USERNAME = "john"
VALID_PASSWORD = "demo"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Navigate to the login page and return a LoginPage instance."""
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> APIRequestContext:
    context = playwright.request.new_context(
        base_url="https://para.testar.org",
        extra_http_headers={"Accept": "application/json"},
    )
    yield context
    context.dispose()


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Log in as john/demo and return the page already authenticated."""
    lp = LoginPage(page)
    lp.navigate()
    lp.login(VALID_USERNAME, VALID_PASSWORD)
    page.wait_for_load_state("networkidle")
    return page
