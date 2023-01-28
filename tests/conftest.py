import json
from dataclasses import dataclass
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class Config(frozen=True):
    browser: str
    headless: bool
    implicit_wait: int = 10

    def __post_init__(self):
        if self.browser not in ["chrome", "firefox", "edge"]:
            ValueError("Given browser is not supported.")


@pytest.fixture
def config() -> Config:
    path = Path(__file__).parent / "../data/config.json"
    with open(path) as file:
        config = json.load(file)
        return Config(**config)


@pytest.fixture
def init_driver(config: Config):
    driver = None

    if config.browser == "chrome":
        driver_exec_path = ChromeDriverManager().install()
        s = Service(driver_exec_path)
        options = Options()
        driver = webdriver.Chrome(service=s)

        if config.headless:
            options.add_argument("--headless")

    return driver
