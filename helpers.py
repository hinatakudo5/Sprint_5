import random
import string
import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, RegisterPageLocators, LoginPageLocators


def _loc(cls, *names):
    for name in names:
        if hasattr(cls, name):
            return getattr(cls, name)
    return None


def generate_email(domain: str = "ya.ru") -> str:
    login = uuid.uuid4().hex[:10]
    return f"{login}@{domain}"


def generate_password(length: int = 10) -> str:
    if length < 6:
        length = 6

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    all_chars = lower + upper + digits

    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
    ]

    password_chars += random.choices(all_chars, k=length - len(password_chars))
    random.shuffle(password_chars)
    return "".join(password_chars)


def generate_name() -> str:
    return f"User{random.randint(1000, 9999)}"


def login_user(driver, email: str, password: str) -> None:
    wait = WebDriverWait(driver, 15)

    email_input = _loc(LoginPageLocators, "EMAIL_INPUT", "EMAIL_FIELD", "EMAIL")
    password_input = _loc(LoginPageLocators, "PASSWORD_INPUT", "PASSWORD_FIELD", "PASSWORD")

    # кнопка "Войти" — берём по тексту, чтобы не зависеть от имени локатора
    login_btn_fallback = (By.XPATH, "//button[contains(., 'Войти')]")

    wait.until(EC.visibility_of_element_located(email_input)).send_keys(email)
    wait.until(EC.visibility_of_element_located(password_input)).send_keys(password)
    wait.until(EC.element_to_be_clickable(login_btn_fallback)).click()


def register_user(driver, name: str, email: str, password: str) -> None:
    wait = WebDriverWait(driver, 15)

    driver.get(f"{BASE_URL}/register")

    name_input = _loc(RegisterPageLocators, "NAME_INPUT", "NAME_FIELD", "NAME")
    email_input = _loc(RegisterPageLocators, "EMAIL_INPUT", "EMAIL_FIELD", "EMAIL")
    password_input = _loc(RegisterPageLocators, "PASSWORD_INPUT", "PASSWORD_FIELD", "PASSWORD")

    # кнопка "Зарегистрироваться" — берём по тексту
    register_btn_fallback = (By.XPATH, "//button[contains(., 'Зарегистрироваться')]")

    wait.until(EC.visibility_of_element_located(name_input)).send_keys(name)
    wait.until(EC.visibility_of_element_located(email_input)).send_keys(email)
    wait.until(EC.visibility_of_element_located(password_input)).send_keys(password)
    wait.until(EC.element_to_be_clickable(register_btn_fallback)).click()

    # если после регистрации перекидывает на /login — логинимся
    try:
        wait.until(EC.url_contains("/login"))
        login_user(driver, email, password)
    except Exception:
        pass
