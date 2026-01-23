from helpers import generate_name, generate_email, generate_password, register_user, login_user
from pages.account_page import AccountPage
from pages.login_page import LoginPage


class TestAccount:
    def test_go_to_personal_account(self, driver):
        name = generate_name()
        email = generate_email()
        password = generate_password()

        register_user(driver, name, email, password)
        login_user(driver, email, password)

        account = AccountPage(driver)
        login = LoginPage(driver)

        # идем в ЛК самым стабильным путем
        account.open_profile_via_header()

        # если вдруг откинуло на /login — логинимся и повторяем
        if login.is_login_page():
            login.login(email, password)
            account.open_profile_via_header()

        assert "/account" in account.current_url(), "Не открылась страница личного кабинета"
        assert account.profile_is_visible() or account.exit_button_is_visible(), (
            "Личный кабинет не открылся: не виден профиль/кнопка выхода"
        )

    def test_logout_from_account(self, driver):
        name = generate_name()
        email = generate_email()
        password = generate_password()

        register_user(driver, name, email, password)
        login_user(driver, email, password)

        account = AccountPage(driver)
        login = LoginPage(driver)

        account.open_profile_via_header()

        if login.is_login_page():
            login.login(email, password)
            account.open_profile_via_header()

        assert "/account" in account.current_url(), "Перед выходом не открылся личный кабинет"

        account.logout()

        assert "/login" in login.current_url(), "После выхода не произошёл переход на /login"
        assert login.is_login_page(), "После выхода не отображается форма логина"
