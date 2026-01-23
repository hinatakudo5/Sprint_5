from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def current_url(self) -> str:
        return self.driver.current_url

    def wait_url_contains(self, part: str) -> None:
        self.wait.until(EC.url_contains(part))

    def wait_url_to_be(self, url: str) -> None:
        self.wait.until(EC.url_to_be(url))

    def is_present(self, locator) -> bool:
        try:
            return len(self.driver.find_elements(*locator)) > 0
        except Exception:
            return False

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def safe_click(self, locator) -> None:
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)

        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            el = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", el)
