from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome('driver/chromedriver.exe')
    return driver