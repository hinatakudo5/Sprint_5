from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, RegisterPageLocators
from helpers import generate_email, generate_password, generate_name


def test_successful_registration(driver):
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME)).send_keys(generate_name())
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.EMAIL)).send_keys(generate_email(domain="ya.ru"))
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD)).send_keys(generate_password())

    wait.until(EC.element_to_be_clickable(RegisterPageLocators.SUBMIT)).click()

    # успешная регистрация ведет на /login
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url


def test_registration_shows_error_for_short_password(driver):
    driver.get(f"{BASE_URL}/register")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.visibility_of_element_located(RegisterPageLocators.NAME)).send_keys(generate_name())
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.EMAIL)).send_keys(generate_email(domain="ya.ru"))
    wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD)).send_keys("12345")  # < 6

    wait.until(EC.element_to_be_clickable(RegisterPageLocators.SUBMIT)).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Некорректный пароль')]")))
