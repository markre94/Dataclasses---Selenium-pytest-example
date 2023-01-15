import json
from pathlib import Path

from pages.form_page import FormRegistrationPage
from model.student import Student
from time import sleep


def load_students_data() -> Student:
    path = Path(__file__).parent / "../data/students.json"
    with open(path) as f:
        return Student(**json.load(f))


def test_register_student(driver):
    form_page = FormRegistrationPage(driver, url="https://demoqa.com/automation-practice-form")
    form_page.input_name("Bronek")
    sleep(10)
