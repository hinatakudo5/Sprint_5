import pytest

from locators import BASE_URL, MainPageLocators
from pages.main_page import MainPage
from pages.account_page import AccountPage


class TestConstructor:
    def test_go_to_constructor_from_account(self, driver):
        account = AccountPage(driver)
        main = MainPage(driver)

        account.open_account()
        account.go_to_constructor()

        account.wait_url_to_be(f"{BASE_URL}/")
        main.tab_is_visible(MainPageLocators.TAB_BUNS)

    def test_go_to_constructor_by_logo(self, driver):
        account = AccountPage(driver)
        main = MainPage(driver)

        account.open_account()
        account.click_logo()

        account.wait_url_to_be(f"{BASE_URL}/")
        main.tab_is_visible(MainPageLocators.TAB_BUNS)

    @pytest.mark.parametrize(
        "tab_locator, active_tab_locator, should_click",
        [
            (MainPageLocators.TAB_BUNS, MainPageLocators.ACTIVE_TAB_BUNS, False),
            (MainPageLocators.TAB_SAUCES, MainPageLocators.ACTIVE_TAB_SAUCES, True),
            (MainPageLocators.TAB_FILLINGS, MainPageLocators.ACTIVE_TAB_FILLINGS, True),
        ],
    )
    def test_constructor_tab_opens(self, driver, tab_locator, active_tab_locator, should_click):
        main = MainPage(driver)

        main.open_main()
        main.tab_is_visible(tab_locator)

        if should_click:
            main.open_tab(tab_locator, safe=True)

        main.tab_is_visible(active_tab_locator)
