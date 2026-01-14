import random
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    BASE_URL,
    RegisterPageLocators,
    LoginPageLocators,
    MainPageLocators,
)


def _first_existing_locator(cls, possible_names: tuple[str, ...]):
    """
    Возвращает первый существующий локатор из cls по списку имён.
    Если не найден — возвращает None.
    """
    for name in possible_names:
        if hasattr(cls, name):
            return getattr(cls, name)
    return None


# ---------- генераторы данных ----------

def generate_email(domain="ya.ru"):
    login = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{login}@{domain}"


def generate_password(length: int = 10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=max(length, 6)))


def generate_name():
    return f"User{random.randint(1000, 9999)}"


# ---------- действия ----------

def register_user(driver, name: str, email: str, password: str) -> None:
    wait = WebDriverWait(driver, 15)
    driver.get(f"{BASE_URL}/register")

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME)).send_keys(name)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD)).send_keys(password)

    # ✅ 1) пробуем найти кнопку регистрации в твоих локаторах (любое популярное имя)
    register_button_locator = _first_existing_locator(
        RegisterPageLocators,
        (
            "REGISTER",
            "REGISTER_BUTTON",
            "SUBMIT",
            "SUBMIT_BUTTON",
            "BUTTON_REGISTER",
            "REGISTRATION_BUTTON",
        ),
    )

    # ✅ 2) если в локаторах нет — кликаем по тексту кнопки
    if register_button_locator is None:
        register_button_locator = (
            "xpath",
            "//button[contains(., 'Зарегистрироваться')]",
        )

    wait.until(EC.element_to_be_clickable(register_button_locator)).click()


def login_user(driver, email: str, password: str) -> None:
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD)).send_keys(password)

    # обычно это есть в локаторах, но на всякий случай сделаем fallback
    login_button_locator = _first_existing_locator(
        LoginPageLocators,
        (
            "LOGIN_BUTTON",
            "SUBMIT_BUTTON",
            "ENTER_BUTTON",
            "LOGIN",
        ),
    )

    if login_button_locator is None:
        login_button_locator = (
            "xpath",
            "//button[contains(., 'Войти')]",
        )

    wait.until(EC.element_to_be_clickable(login_button_locator)).click()


def assert_logged_in(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT))
