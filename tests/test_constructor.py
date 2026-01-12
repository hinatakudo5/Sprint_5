import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MainPageLocators, AccountPageLocators


def test_go_to_constructor_from_account(driver):
    wait = WebDriverWait(driver, 15)

    driver.get(f"{BASE_URL}/account")
    wait.until(EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_LINK)).click()

    wait.until(EC.url_to_be(f"{BASE_URL}/"))
    wait.until(EC.visibility_of_element_located(MainPageLocators.TAB_BUNS))


def test_go_to_constructor_by_logo(driver):
    wait = WebDriverWait(driver, 15)

    driver.get(f"{BASE_URL}/account")
    wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGO)).click()

    wait.until(EC.url_to_be(f"{BASE_URL}/"))
    wait.until(EC.visibility_of_element_located(MainPageLocators.TAB_BUNS))


@pytest.mark.parametrize(
    "tab_locator, active_tab_locator, needs_click",
    [
        (MainPageLocators.TAB_BUNS, MainPageLocators.ACTIVE_TAB_BUNS, False),
        (MainPageLocators.TAB_SAUCES, MainPageLocators.ACTIVE_TAB_SAUCES, True),
        (MainPageLocators.TAB_FILLINGS, MainPageLocators.ACTIVE_TAB_FILLINGS, True),
    ],
)
def test_constructor_tab_opens(driver, tab_locator, active_tab_locator, needs_click):
    wait = WebDriverWait(driver, 15)

    driver.get(BASE_URL)

    if needs_click:
        wait.until(EC.element_to_be_clickable(tab_locator)).click()

    wait.until(EC.visibility_of_element_located(active_tab_locator))
