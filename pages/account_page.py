from pages.base_page import BasePage
from locators import BASE_URL, AccountPageLocators


class AccountPage(BasePage):
    def open_account(self) -> None:
        self.open(f"{BASE_URL}/account")

    def go_to_constructor(self) -> None:
        self.click(AccountPageLocators.CONSTRUCTOR_LINK)

    def click_logo(self) -> None:
        self.click(AccountPageLocators.LOGO)
