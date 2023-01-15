import datetime
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path


@dataclass
class Student:
    name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime
    subjects: list[str]
    hobbies: list[str]
    picture: str
    current_address: str
    state: str
    city: str

    def __post_init__(self):
        self._validate_data()

    def __validate_state(self):
        pass

    def __validate_city(self):
        pass

    def __validate_picture_path(self):
        pass

    def _validate_data(self):
        self.__validate_state()
        self.__validate_city()
        self.__validate_picture_path()
