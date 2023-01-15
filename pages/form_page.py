from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from model.student import Student


class StudentRegistrationLocators:
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    EMAIL = (By.ID, 'userEmail')
    GENDER = (By.ID, 'genterWrapper')
    MOBILE = (By.ID, 'userNumber')
    DATE_OF_BIRTH = (By.ID, 'dateOfBirthInput')
    SUBJECTS = (By.ID, 'subjectsContainer')
    HOBBIES = (By.ID, 'hobbiesWrapper')
    PICTURE = (By.ID, 'uploadPicture')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    STATE = (By.ID, 'state')
    CITY = (By.ID, 'city')
    SUBMIT = (By.ID, 'submit')


class FormRegistrationPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.locators = StudentRegistrationLocators()

    def input_name(self, name: str):
        self.find_element(*self.locators.FIRST_NAME).send_keys(name)

    def input_last_name(self, last_name):
        self.find_element(*self.locators.LAST_NAME).send_keys(last_name)

    def input_email(self):
        pass

    def select_gender(self):
        pass

    def input_mobile(self):
        pass

    def select_date_of_birth(self):
        pass

    def input_subjects(self):
        pass

    def select_hobbies(self):
        pass

    def select_picture(self):
        pass

    def input_current_address(self):
        pass

    def select_state(self):
        pass

    def select_city(self):
        pass

    def register_form(self, student: Student):
        pass

    def click_submit(self):
        self.find_element(*self.locators.SUBMIT).click()
