from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://para.testar.org"

    def __init__(self, page: Page) -> None:
        self.page = page

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

    def wait_for_load(self) -> None:
        self.page.wait_for_load_state("networkidle")
