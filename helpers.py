import random
import string
import uuid

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegisterPageLocators, LoginPageLocators, BASE_URL


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

    # гарантируем: 1 маленькая, 1 большая, 1 цифра
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
    ]

    password_chars += random.choices(all_chars, k=length - len(password_chars))
    random.shuffle(password_chars)
    return "".join(password_chars)


def generate_name(length: int = 8) -> str:
    letters = string.ascii_letters
    return "".join(random.choices(letters, k=length))


def register_user(driver, name: str, email: str, password: str) -> None:
    """
    Регистрирует пользователя через UI.
    После успешной регистрации страница перекидывает на /login.
    """
    wait = WebDriverWait(driver, 15)

    driver.get(f"{BASE_URL}/register")

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME)).send_keys(name)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD)).send_keys(password)

    wait.until(EC.element_to_be_clickable(RegisterPageLocators.SUBMIT)).click()

    # После регистрации ожидаем форму входа
    wait.until(EC.visibility_of_element_located(LoginPageLocators.SUBMIT))


def login_user(driver, email: str, password: str) -> None:
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL)).send_keys(email)
    wait.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD)).send_keys(password)

    wait.until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT)).click()
