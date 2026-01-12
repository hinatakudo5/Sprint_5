import random
import string
import uuid

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LoginPageLocators


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

    wait.until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    wait.until(
        EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
    ).send_keys(password)

    wait.until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    ).click()
