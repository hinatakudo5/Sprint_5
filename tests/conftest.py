import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # ВАЖНО: явно указываем Chrome
    options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
