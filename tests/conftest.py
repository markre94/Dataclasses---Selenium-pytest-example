from model.config import TestConfig
import pytest
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


@pytest.fixture
def framework_config() -> TestConfig:
    path = Path(__file__).parent / "../data/config.json"
    with open(path) as file:
        config = json.load(file)
        return TestConfig(**config)


def init_chrome_browser(config: TestConfig):
    driver_exec_path = ChromeDriverManager().install()
    s = Service(driver_exec_path)
    options = Options()
    driver = webdriver.Chrome(service=s)

    if config.headless:
        options.add_argument("--headless")

    return driver


def init_firefox_browser(config: TestConfig):
    pass


def init_edge_browser(confi: TestConfig):
    pass


@pytest.fixture()
def driver(framework_config):
    config = framework_config
    driver = None

    if config.browser == "chrome":
        driver_exec_path = ChromeDriverManager().install()
        s = Service(driver_exec_path)
        options = Options()
        options.add_argument("--start-fullscreen")
        driver = webdriver.Chrome(service=s)

        if config.headless:
            options.add_argument("--headless")


    elif config.browser == "firefox":
        pass

    elif config.browser == "edge":
        pass

    yield driver

    driver.close()

# DRIVER_CREATORS = {
#     "chrome": init_chrome_browser,
#     "firefox": init_firefox_browser,
#     "edge": init_edge_browser
# }
#
#
# @pytest.fixture
# def init_driver(framework_config):
#     config = framework_config
#     driver = DRIVER_CREATORS[config.browser](config)
#     yield driver
#     driver.close()
