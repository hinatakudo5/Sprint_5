from locators import BASE_URL, LoginPageLocators, MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open_login(self) -> None:
        self.open(f"{BASE_URL}/login")

    def login(self, email: str, password: str) -> None:
        self.wait.until(lambda d: d.find_element(*LoginPageLocators.EMAIL)).send_keys(email)
        self.wait.until(lambda d: d.find_element(*LoginPageLocators.PASSWORD)).send_keys(password)
        self.safe_click(LoginPageLocators.SUBMIT)

        # признак успешного логина — появляется "Личный Кабинет" в шапке
        self.wait.until(lambda d: len(d.find_elements(*MainPageLocators.PERSONAL_ACCOUNT)) > 0)

    def is_login_page(self) -> bool:
        return "/login" in self.current_url() or self.is_present(LoginPageLocators.SUBMIT)
