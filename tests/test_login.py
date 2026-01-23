import pytest
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL
from helpers import login_user, assert_logged_in
from pages.main_page import MainPage


class TestLogin:
    def test_login_from_main_page_button(self, driver, wait, registered_user):
        email, password = registered_user

        main = MainPage(driver)
        main.open_main()
        main.click_login_from_main()

        # попали на /login
        wait.until(EC.url_contains("/login"))

        login_user(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_personal_account_button(self, driver, registered_user):
        email, password = registered_user

        main = MainPage(driver)
        main.open_main()
        main.go_to_personal_account()

        login_user(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_register_form_link(self, driver, wait, registered_user):
        email, password = registered_user

        driver.get(f"{BASE_URL}/register")
        wait.until(EC.element_to_be_clickable(("xpath", "//a[contains(., 'Войти')]"))).click()

        login_user(driver, email, password)
        assert_logged_in(driver)

    def test_login_from_forgot_password_form_link(self, driver, wait, registered_user):
        email, password = registered_user

        driver.get(f"{BASE_URL}/forgot-password")
        wait.until(EC.element_to_be_clickable(("xpath", "//a[contains(., 'Войти')]"))).click()

        login_user(driver, email, password)
        assert_logged_in(driver)
