from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_main(self):
        self.driver.get(f"{BASE_URL}/")

    def click_login_from_main(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

    def click_personal_account(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT)
        ).click()

    # 🔹 метод ИМЕННО под твой тест
    def go_to_personal_account(self):
        self.click_personal_account()

    def open_tab(self, tab_locator):
        self.wait.until(EC.element_to_be_clickable(tab_locator)).click()

    def tab_is_visible(self, tab_locator):
        self.wait.until(EC.visibility_of_element_located(tab_locator))
