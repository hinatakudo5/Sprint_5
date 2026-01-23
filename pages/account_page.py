from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import BASE_URL, AccountPageLocators, MainPageLocators


class AccountPage:
    # Более широкие "якоря" личного кабинета (на случай, если открылось не /profile, а /orders)
    PROFILE_TEXT_ANY = (By.XPATH, "//*[contains(normalize-space(),'Профиль')]")
    ORDERS_TEXT_ANY = (By.XPATH, "//*[contains(normalize-space(),'История заказов')]")
    ACCOUNT_MENU_ANY = (
        By.XPATH,
        "//a[contains(@href,'/account/profile') or contains(@href,'/account/order')]"
        " | //button[contains(normalize-space(),'Выход')]"
        " | //*[contains(normalize-space(),'История заказов')]"
        " | //*[contains(normalize-space(),'Профиль')]",
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def current_url(self):
        return self.driver.current_url

    def wait_url_to_be(self, url: str):
        self.wait.until(EC.url_to_be(url))

    def open_account(self):
        self.driver.get(f"{BASE_URL}/account")

    def open_profile_via_header(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
        ).click()

    def _wait_account_loaded_short(self, timeout: int = 7) -> bool:
        """
        Короткое ожидание, что ЛК реально прогрузился (любой якорь: профиль/заказы/выход/меню).
        Возвращает True/False, без падения.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.ACCOUNT_MENU_ANY)
            )
            return True
        except TimeoutException:
            return False

    def profile_is_visible(self):
        # Ждём чуть-чуть прогрузку ЛК, иначе иногда проверка слишком ранняя
        self._wait_account_loaded_short(timeout=7)

        # 1) текст "Профиль"
        if len(self.driver.find_elements(*self.PROFILE_TEXT_ANY)) > 0:
            return True

        # 2) ссылка на профиль (если есть)
        if len(self.driver.find_elements(*AccountPageLocators.PROFILE_LINK)) > 0:
            return True

        # 3) если открылся раздел "История заказов" — это тоже ЛК (тесту достаточно, что ЛК открылся)
        if len(self.driver.find_elements(*self.ORDERS_TEXT_ANY)) > 0:
            return True

        return False

    def exit_button_is_visible(self):
        # Ждём чуть-чуть прогрузку ЛК
        self._wait_account_loaded_short(timeout=7)
        return len(self.driver.find_elements(*AccountPageLocators.EXIT_BUTTON)) > 0

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(AccountPageLocators.EXIT_BUTTON)
        ).click()

        # после выхода должно перекинуть на /login
        self.wait.until(EC.url_contains("/login"))

    def go_to_constructor(self):
        self.wait.until(
            EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_LINK)
        ).click()

    def click_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(AccountPageLocators.LOGO)
        ).click()
