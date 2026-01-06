import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import BASE_URL, MainPageLocators


# ========= ЛОКАТОРЫ (с запасными вариантами) =========

# Заголовок страницы регистрации — чтобы дождаться, что мы точно на нужной странице
REGISTER_HEADER = (By.XPATH, "//*[contains(text(),'Регистрация')]")

# Имя: сначала как name="name" (у тебя это работает), + запасной вариант по тексту "Имя"
NAME_INPUT = (
    By.XPATH,
    "//input[@name='name'] | //label[contains(.,'Имя')]/following::input[1] | //p[contains(.,'Имя')]/following::input[1]"
)

# Email: сначала type=email (если есть), иначе по тексту "Email"
EMAIL_INPUT = (
    By.XPATH,
    "//input[@type='email'] | //label[contains(.,'Email')]/following::input[1] | //p[contains(.,'Email')]/following::input[1]"
)

# Пароль: обычно это единственный input type=password
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")
LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")
LOGIN_LINK = (By.XPATH, "//a[contains(.,'Войти')]")


# ========= ДАННЫЕ ДЛЯ ТЕСТОВ =========
def generate_name() -> str:
    return "Zarina"


def generate_password() -> str:
    # ревьюер просил минимум 6 символов
    return "123456"


def generate_email() -> str:
    # строго "логин@домен" (пример: 123@ya.ru) — делаем безопасный вариант
    login = "user" + "".join(random.choices(string.digits, k=6))
    return f"{login}@ya.ru"


# ========= ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =========
def open_register_page(driver):
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located(REGISTER_HEADER))
    return wait


def register_user(driver, email: str, password: str):
    wait = open_register_page(driver)

    wait.until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(generate_name())
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(password)

    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()


def login_user(driver, email: str, password: str):
    wait = WebDriverWait(driver, 15)

    # тут мы используем те же EMAIL_INPUT / PASSWORD_INPUT,
    # потому что форма входа визуально очень похожа и обычно совпадает по структуре
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()


def assert_logged_in(driver):
    wait = WebDriverWait(driver, 15)
    # после успешного входа на главной видна кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//button[contains(.,'Оформить заказ')]")
    ))


# ========= ТЕСТЫ =========
def test_login_from_main_page_button(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email()
    password = generate_password()

    register_user(driver, email, password)

    # чтобы точно быть "не залогиненой"
    driver.delete_all_cookies()

    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()

    login_user(driver, email, password)
    assert_logged_in(driver)


def test_login_from_personal_account_button(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email()
    password = generate_password()

    register_user(driver, email, password)

    driver.delete_all_cookies()
    driver.get(BASE_URL)

    wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

    login_user(driver, email, password)
    assert_logged_in(driver)


def test_login_from_register_form_link(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email()
    password = generate_password()

    register_user(driver, email, password)

    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/register")

    wait.until(EC.element_to_be_clickable(LOGIN_LINK)).click()

    login_user(driver, email, password)
    assert_logged_in(driver)


def test_login_from_forgot_password_form_link(driver):
    wait = WebDriverWait(driver, 15)
    email = generate_email()
    password = generate_password()

    register_user(driver, email, password)

    driver.delete_all_cookies()
    driver.get(f"{BASE_URL}/forgot-password")

    wait.until(EC.element_to_be_clickable(LOGIN_LINK)).click()

    login_user(driver, email, password)
    assert_logged_in(driver)
