from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import BASE_URL
from tests.helpers import generate_email, generate_password, generate_name


# Универсальные локаторы: ищем input "после" label в DOM
NAME_INPUT = (By.XPATH, "//label[contains(.,'Имя')]/following::input[1]")
EMAIL_INPUT = (By.XPATH, "//label[contains(.,'Email')]/following::input[1]")
PASSWORD_INPUT = (By.XPATH, "//label[contains(.,'Пароль')]/following::input[1]")

REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Зарегистрироваться')]")
LOGIN_TITLE = (By.XPATH, "//*[contains(text(),'Вход')]")


def test_successful_registration(driver):
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 10)

    # Заполняем поля
    wait.until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(generate_name())
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(generate_email())
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys(generate_password())

    # Клик "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # После успешной регистрации попадаем на страницу входа
    wait.until(EC.visibility_of_element_located(LOGIN_TITLE))
    assert "/login" in driver.current_url


def test_registration_shows_error_for_short_password(driver):
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 10)

    # Заполняем поля, пароль < 6 символов
    wait.until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(generate_name())
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(generate_email())
    wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("12345")

    # ВАЖНО: клик, чтобы сработала валидация
    wait.until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # Ждем ошибку "Некорректный пароль"
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(.,'Некорректный пароль')]")
        )
    )
