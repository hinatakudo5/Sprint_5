import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from locators import BASE_URL, MainPageLocators, AccountPageLocators


def _safe_click(driver, locator, timeout: int = 15) -> None:
    """Клик с подстраховкой: скролл к элементу + JS-клик если перехватывает другой элемент."""
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    try:
        wait.until(EC.element_to_be_clickable(locator)).click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", element)


def test_go_to_constructor_from_account(driver):
    """
    Переход из личного кабинета в конструктор:
    Переход по клику на «Конструктор» - работает.
    """
    wait = WebDriverWait(driver, 15)
    driver.get(f"{BASE_URL}/account")

    wait.until(EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_LINK)).click()
    wait.until(EC.url_to_be(f"{BASE_URL}/"))
    wait.until(EC.visibility_of_element_located(MainPageLocators.TAB_BUNS))


def test_go_to_constructor_by_logo(driver):
    """
    Переход из личного кабинета в конструктор:
    Переход по клику на логотип Stellar Burgers - работает.
    """
    wait = WebDriverWait(driver, 15)
    driver.get(f"{BASE_URL}/account")

    wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGO)).click()
    wait.until(EC.url_to_be(f"{BASE_URL}/"))
    wait.until(EC.visibility_of_element_located(MainPageLocators.TAB_BUNS))


@pytest.mark.parametrize(
    "tab_locator, active_tab_locator, should_click",
    [
        # “Булки” обычно активны по умолчанию → НЕ кликаем, только проверяем активность
        (MainPageLocators.TAB_BUNS, MainPageLocators.ACTIVE_TAB_BUNS, False),

        # Эти табы нужно открывать кликом
        (MainPageLocators.TAB_SAUCES, MainPageLocators.ACTIVE_TAB_SAUCES, True),
        (MainPageLocators.TAB_FILLINGS, MainPageLocators.ACTIVE_TAB_FILLINGS, True),
    ],
)
def test_constructor_tab_opens(driver, tab_locator, active_tab_locator, should_click):
    """
    Раздел «Конструктор»:
    Открытие каждой табы — отдельный параметризованный тест.
    """
    wait = WebDriverWait(driver, 15)
    driver.get(BASE_URL)

    # табы должны быть видны
    wait.until(EC.visibility_of_element_located(tab_locator))

    if should_click:
        _safe_click(driver, tab_locator)

    wait.until(EC.visibility_of_element_located(active_tab_locator))
