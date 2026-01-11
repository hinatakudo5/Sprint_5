from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.education-services.ru"


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]/ancestor::a")

    TAB_BUNS = (By.XPATH, "//span[text()='Булки']")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']")
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']")

    ACTIVE_TAB_BUNS = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span[text()='Булки']")
    ACTIVE_TAB_SAUCES = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span[text()='Соусы']")
    ACTIVE_TAB_FILLINGS = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span[text()='Начинки']")

    # “Оформить заказ” появляется, когда пользователь залогинен (для проверки успешного входа)
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")


class LoginPageLocators:
    # Надежные локаторы: по label → input
    EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Войти')]")

    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    RECOVER_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")


class RegisterPageLocators:
    NAME = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")
    EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

    # ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]/ancestor::a")
    LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")
