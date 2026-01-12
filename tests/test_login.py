from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MainPageLocators, LoginPageLocators
from helpers import generate_email, generate_password, generate_name, login_user


def test_login_from_main_page_button(driver):
    wait = WebDriverWait(driver, 15)

    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL)

    wait.until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
    ).click()

    login_user(driver, email, password)

    wait.until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )


def test_login_from_personal_account_button(driver):
    wait = WebDriverWait(driver, 15)

    email = generate_email()
    password = generate_password()

    driver.get(BASE_URL)

    wait.until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
    ).click()

    login_user(driver, email, password)

    wait.until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )


def test_login_from_register_form_link(driver):
    wait = WebDriverWait(driver, 15)

    email = generate_email()
    password = generate_password()

    driver.get(f"{BASE_URL}/register")

    wait.until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
    ).click()

    login_user(driver, email, password)

    wait.until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )


def test_login_from_forgot_password_form_link(driver):
    wait = WebDriverWait(driver, 15)

    email = generate_email()
    password = generate_password()

    driver.get(f"{BASE_URL}/forgot-password")

    wait.until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
    ).click()

    login_user(driver, email, password)

    wait.until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
    )
