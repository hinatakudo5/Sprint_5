# helpers.py
import random
import string
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    BASE_URL,
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
)


# -------------------------
# Генераторы тест-данных
# -------------------------
def generate_name(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return "user_" + "".join(random.choice(letters) for _ in range(length))


def generate_email(domain: str = "ya.ru") -> str:
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for _ in range(10)) + f"@{domain}"


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


# -------------------------
# Базовые действия
# -------------------------
def register_user(driver, name: str, email: str, password: str):
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME)).send_keys(name)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD)).send_keys(password)

    # небольшая пауза на валидацию формы
    time.sleep(0.2)

    wait.until(EC.element_to_be_clickable(RegisterPageLocators.SUBMIT)).click()

    # после успешной регистрации обычно редиректит на /login
    WebDriverWait(driver, 20).until(lambda d: "/login" in d.current_url)


def login_user(driver, email: str, password: str):
    driver.get(f"{BASE_URL}/login")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD)).send_keys(password)

    time.sleep(0.2)

    wait.until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT)).click()

    # после логина чаще всего кидает на /
    WebDriverWait(driver, 20).until(lambda d: d.current_url.startswith(f"{BASE_URL}/"))


def assert_logged_in(driver):
    """
    Универсальная проверка логина:
    - появляется кнопка "Оформить заказ" (на главной)
    """
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located(("xpath", "//*[normalize-space()='Оформить заказ']")))


def logout_user(driver):
    """
    Если тебе нужно из helper — выход можно сделать через кнопку Выход,
    но у тебя это обычно проверяется через PageObject в account тестах.
    """
    from locators import AccountPageLocators  # чтобы не было циклических импортов

    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)).click()
    WebDriverWait(driver, 20).until(lambda d: "/login" in d.current_url)
