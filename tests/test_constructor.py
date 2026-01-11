from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MainPageLocators, AccountPageLocators
from helpers import generate_email, generate_password, generate_name, register_user


def test_go_to_constructor_from_account(driver):
    wait = WebDriverWait(driver, 15)

    name = generate_name()
    email = generate_email(domain="ya.ru")
    password = generate_password()

    register_user(driver, name, email, password)

    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()
    wait.until(EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_LINK)).click()

    wait.until(EC.url_to_be(BASE_URL + "/"))
    assert driver.current_url == BASE_URL + "/"


def test_go_to_constructor_by_logo(driver):
    wait = WebDriverWait(driver, 15)

    name = generate_name()
    email = generate_email(domain="ya.ru")
    password = generate_password()

    register_user(driver, name, email, password)

    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()
    wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGO)).click()

    wait.until(EC.url_to_be(BASE_URL + "/"))
    assert driver.current_url == BASE_URL + "/"


def test_constructor_tabs_work(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(BASE_URL)

    wait.until(EC.element_to_be_clickable(MainPageLocators.TAB_SAUCES)).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB_SAUCES))

    wait.until(EC.element_to_be_clickable(MainPageLocators.TAB_FILLINGS)).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB_FILLINGS))

    wait.until(EC.element_to_be_clickable(MainPageLocators.TAB_BUNS)).click()
    wait.until(EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB_BUNS))
