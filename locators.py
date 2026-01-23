# locators.py
from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.education-services.ru"


def _input_by_label(text: str):
    """
    Универсальный XPath для инпута по label:
    - либо input как following-sibling
    - либо input внутри того же контейнера
    """
    xp = (
        f"//label[normalize-space()='{text}']/following-sibling::input"
        f" | //label[normalize-space()='{text}']/..//input"
    )
    return (By.XPATH, xp)


class MainPageLocators:
    # Главная
    LOGIN_BUTTON = (By.XPATH, "//button[.//*[normalize-space()='Войти в аккаунт'] or normalize-space()='Войти в аккаунт']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[normalize-space()='Личный Кабинет']/ancestor::a")

    # Табы конструктора
    TAB_BUNS = (By.XPATH, "//span[normalize-space()='Булки']")
    TAB_SAUCES = (By.XPATH, "//span[normalize-space()='Соусы']")
    TAB_FILLINGS = (By.XPATH, "//span[normalize-space()='Начинки']")

    # Активные табы
    ACTIVE_TAB_BUNS = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[normalize-space()='Булки']")
    ACTIVE_TAB_SAUCES = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[normalize-space()='Соусы']")
    ACTIVE_TAB_FILLINGS = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span[normalize-space()='Начинки']")


class LoginPageLocators:
    EMAIL = _input_by_label("Email")
    PASSWORD = _input_by_label("Пароль")

    # кнопка "Войти"
    SUBMIT = (By.XPATH, "//button[.//*[normalize-space()='Войти'] or normalize-space()='Войти']")

    # ✅ синонимы для helpers._loc()
    LOGIN_BUTTON = SUBMIT
    SUBMIT_BUTTON = SUBMIT
    ENTER_BUTTON = SUBMIT

    # ссылка "Войти" (на /register и /forgot-password)
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Войти']")


class RegisterPageLocators:
    NAME = _input_by_label("Имя")
    EMAIL = _input_by_label("Email")
    PASSWORD = _input_by_label("Пароль")

    # кнопка "Зарегистрироваться"
    SUBMIT = (By.XPATH, "//button[.//*[normalize-space()='Зарегистрироваться'] or normalize-space()='Зарегистрироваться']")

    # ✅ синонимы для helpers._loc()
    REGISTER_BUTTON = SUBMIT
    SUBMIT_BUTTON = SUBMIT
    SAVE_BUTTON = SUBMIT


class AccountPageLocators:
    # профиль в меню
    PROFILE_LINK = (By.XPATH, "//a[contains(@href,'/account/profile')]")

    # кнопка "Выход"
    EXIT_BUTTON = (By.XPATH, "//button[.//*[normalize-space()='Выход'] or normalize-space()='Выход']")

    # верхнее меню
    CONSTRUCTOR_LINK = (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")
