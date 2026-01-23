import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from helpers import generate_email, generate_password, generate_name, register_user


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # важно для codespaces
    options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)


@pytest.fixture
def registered_user(driver):
    """
    Предусловие для тестов логина:
    1) регистрируем нового пользователя
    2) чистим cookies, чтобы он стал "разлогинен"
    3) возвращаем email/password для логина
    """
    name = generate_name()
    email = generate_email()
    password = generate_password()

    register_user(driver, name, email, password)

    # чтобы тесты логина гарантированно начинались в "неавторизованном" состоянии
    driver.delete_all_cookies()

    return email, password
