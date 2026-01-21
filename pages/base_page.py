from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def safe_click(self, locator) -> None:
        """
        Клик с подстраховкой:
        - ждём присутствие
        - скроллим к элементу
        - кликаем обычным кликом
        - если перехватывает другой элемент -> JS click
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def is_visible(self, locator) -> bool:
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    def wait_url_to_be(self, url: str) -> None:
        self.wait.until(EC.url_to_be(url))
