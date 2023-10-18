import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")

    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options)
        print("Running in Headless Mode Chrome Browser")

    driver.maximize_window()
    driver.get("https://www.ebay.com/")
    return driver
