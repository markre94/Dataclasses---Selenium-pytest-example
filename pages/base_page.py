from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    @property
    def page_title(self) -> str:
        return self.driver.title
