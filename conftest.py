import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

VALID_USERNAME = "john"
VALID_PASSWORD = "demo"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Navigate to the login page and return a LoginPage instance."""
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """Log in as john/demo and return the page already authenticated."""
    lp = LoginPage(page)
    lp.navigate()
    lp.login(VALID_USERNAME, VALID_PASSWORD)
    page.wait_for_load_state("networkidle")
    return page
