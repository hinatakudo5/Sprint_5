import pytest
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MainPageLocators, LoginPageLocators
from helpers import login_user, assert_logged_in


class TestLogin:
    def test_login_from_main_page_button(self, driver, wait, registered_user):
        email, password = registered_user

        driver.get(BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()

        login_user(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_personal_account_button(self, driver, wait, registered_user):
        email, password = registered_user

        driver.get(BASE_URL)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

        login_user(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_register_form_link(self, driver, wait, registered_user):
        email, password = registered_user

        driver.get(f"{BASE_URL}/register")
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)).click()

        login_user(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_forgot_password_form_link(self, driver, wait, registered_user):
        email, password = registered_user

        driver.get(f"{BASE_URL}/forgot-password")
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)).click()

        login_user(driver, email, password)
        assert_logged_in(driver)
