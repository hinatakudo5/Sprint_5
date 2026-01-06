from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import BASE_URL, MainPageLocators, AccountPageLocators


def test_go_to_constructor_from_account(driver):
    """
    4) Переход из личного кабинета в конструктор:
    Переход по клику на «Конструктор» - работает.
    """
    wait = WebDriverWait(driver, 15)

    driver.get(f"{BASE_URL}/account")

    wait.until(EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_LINK)).click()
    wait.until(EC.url_to_be(f"{BASE_URL}/"))

    # на главной странице видим кнопку "Оформить заказ" или хотя бы вкладки конструктора
    wait.until(EC.visibility_of_element_located(MainPageLocators.TAB_BUNS))


def test_go_to_constructor_by_logo(driver):
    """
    4) Переход из личного кабинета в конструктор:
    Переход по клику на логотип Stellar Burgers - работает.
    """
    wait = WebDriverWait(driver, 15)

    driver.get(f"{BASE_URL}/account")

    wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGO)).click()
    wait.until(EC.url_to_be(f"{BASE_URL}/"))
    wait.until(EC.visibility_of_element_located(MainPageLocators.TAB_BUNS))


def test_constructor_tabs_work(driver):
    """
    6) Раздел «Конструктор»:
    Переходы к разделам «Булки», «Соусы», «Начинки» - работают.
    """
    wait = WebDriverWait(driver, 15)
    driver.get(BASE_URL)

    # Соусы
    wait.until(EC.element_to_be_clickable(MainPageLocators.TAB_SAUCES)).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB_SAUCES))

    # Начинки
    wait.until(EC.element_to_be_clickable(MainPageLocators.TAB_FILLINGS)).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB_FILLINGS))

    # Булки
    wait.until(EC.element_to_be_clickable(MainPageLocators.TAB_BUNS)).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB_BUNS))
