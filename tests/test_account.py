from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import (
    BASE_URL,
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    AccountPageLocators,
)
from tests.helpers import generate_email, generate_password, generate_name


def register_user(driver, email, password):
    wait = WebDriverWait(driver, 15)
    driver.get(f"{BASE_URL}/register")

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME)).send_keys(generate_name())
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD)).send_keys(password)
    wait.until(EC.element_to_be_clickable(RegisterPageLocators.SUBMIT)).click()

    # успешная регистрация ведёт на /login
    wait.until(EC.url_contains("/login"))


def login_user(driver, email, password):
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD)).send_keys(password)
    wait.until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT)).click()

    # успешный вход: появилась кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON))


def test_go_to_personal_account(driver):
    """
    3) Переход в личный кабинет:
    Переход по клику на «Личный кабинет» - работает.
    """
    wait = WebDriverWait(driver, 15)
    email = generate_email()
    password = generate_password()

    register_user(driver, email, password)

    # логинимся
    login_user(driver, email, password)

    # кликаем "Личный кабинет"
    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

    # проверяем, что открылась страница профиля (есть ссылка "Профиль")
    wait.until(EC.visibility_of_element_located(AccountPageLocators.PROFILE_LINK))
    assert "/account" in driver.current_url


def test_logout_from_account(driver):
    """
    5) Выход из аккаунта:
    Проверь выход по кнопке «Выйти» в личном кабинете - работает.
    Выводит на страницу Входа.
    """
    wait = WebDriverWait(driver, 15)
    email = generate_email()
    password = generate_password()

    register_user(driver, email, password)
    login_user(driver, email, password)

    # идём в личный кабинет
    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()
    wait.until(EC.visibility_of_element_located(AccountPageLocators.PROFILE_LINK))

    # нажимаем "Выход"
    wait.until(EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)).click()

    # после выхода должна быть страница логина
    wait.until(EC.url_contains("/login"))
    wait.until(EC.visibility_of_element_located(LoginPageLocators.SUBMIT))
    assert "/login" in driver.current_url
