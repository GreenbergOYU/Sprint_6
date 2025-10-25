import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import UrlData


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(UrlData.URL)
    yield driver
    driver.quit()