from pages.base_page import BasePage
from locators import BASE_URL, MainPageLocators


class MainPage(BasePage):
    def open_main(self) -> None:
        self.open(BASE_URL)

    def tab_is_visible(self, tab_locator) -> None:
        self.is_visible(tab_locator)

    def open_tab(self, tab_locator, safe: bool = False) -> None:
        if safe:
            self.safe_click(tab_locator)
        else:
            self.click(tab_locator)
