from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (
    BASE_URL,
    MainPageLocators,
    AccountPageLocators,
    LoginPageLocators,
)
from helpers import (
    generate_name,
    generate_email,
    generate_password,
    register_user,
    login_user,
)


class TestAccount:
    def test_go_to_personal_account(self, driver):
        wait = WebDriverWait(driver, 10)

        name = generate_name()
        email = generate_email()
        password = generate_password()

        # регистрация (после неё пользователь обычно уже авторизован)
        register_user(driver, name, email, password)

        # переходим в Личный кабинет
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

        # если вдруг редиректнуло на логин (так бывает), логинимся и снова открываем ЛК
        if "/login" in driver.current_url:
            login_user(driver, email, password)
            wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

        # ждём появления элемента профиля
        profile_link = wait.until(
            EC.visibility_of_element_located(AccountPageLocators.PROFILE_LINK)
        )

        # ✅ явная проверка, что мы действительно в ЛК (профиль виден)
        assert profile_link.is_displayed(), "Профиль в личном кабинете не отображается"

    def test_logout_from_account(self, driver):
        wait = WebDriverWait(driver, 10)

        name = generate_name()
        email = generate_email()
        password = generate_password()

        register_user(driver, name, email, password)

        # переходим в Личный кабинет
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

        # если редирект на логин — логинимся и снова открываем ЛК
        if "/login" in driver.current_url:
            login_user(driver, email, password)
            wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)).click()

        # выходим
        wait.until(EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)).click()

        # ждём кнопку "Войти" на странице логина
        login_button = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.SUBMIT)
        )

        # ✅ явная проверка, что мы реально разлогинились и попали на /login
        assert "/login" in driver.current_url, "После выхода не произошёл переход на страницу /login"
        assert login_button.is_displayed(), "Кнопка 'Войти' не отображается после выхода"
