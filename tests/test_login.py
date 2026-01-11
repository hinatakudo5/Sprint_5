from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MainPageLocators, LoginPageLocators, RegisterPageLocators
from helpers import generate_email, generate_password, generate_name, register_user, login_user


def assert_logged_in(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON))


def test_login_from_main_page_button(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email(domain="ya.ru")
    password = generate_password()
    name = generate_name()

    register_user(driver, name, email, password)

    driver.delete_all_cookies()
    driver.get(BASE_URL)

    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    login_user(driver, email, password)

    assert_logged_in(driver)


def test_login_from_personal_account_button(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email(domain="ya.ru")
    password = generate_password()
    name = generate_name()

    register_user(driver, name, email, password)

    driver.delete_all_cookies()
    driver.get(BASE_URL)

    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()
    login_user(driver, email, password)

    assert_logged_in(driver)


def test_login_from_register_form_link(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email(domain="ya.ru")
    password = generate_password()
    name = generate_name()

    register_user(driver, name, email, password)

    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/register")

    wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()
    login_user(driver, email, password)

    assert_logged_in(driver)


def test_login_from_forgot_password_form_link(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email(domain="ya.ru")
    password = generate_password()
    name = generate_name()

    register_user(driver, name, email, password)

    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/forgot-password")

    wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)).click()
    login_user(driver, email, password)

    assert_logged_in(driver)
