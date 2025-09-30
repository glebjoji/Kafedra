import json
import re

from src.student_base import StudentBase

class Student(StudentBase):

    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        super().__init__(student_id, last_name, first_name, middle_name, phone_string)
        self._address = Student._validate_address(address)

    @staticmethod
    def _validate_address(address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Адрес должен быть непустой строкой.")

        # Требуем хотя бы одну букву кириллицы
        if not re.search(r"[А-Яа-яЁё]+", address):
            raise ValueError("Адрес должен содержать хотя бы одну кириллическую букву.")
        
        return address
    

        # json и 
    @classmethod
    def from_string(cls, data_string: str):
        parts = [p.strip() for p in data_string.split(',')]
        if len(parts) != 6:
            raise ValueError("Неверный формат строки. Ожидается 6 полей.")
        
        student_id, last_name, first_name, middle_name, address, phone_string = parts
        return cls(int(student_id), last_name, first_name, middle_name, address, phone_string)

    @classmethod
    def from_json(cls, json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        if not isinstance(json_data, dict):
            raise TypeError("Ожидается словарь или JSON-строка.")

        return cls(
            json_data["student_id"],
            json_data["last_name"],
            json_data["first_name"],
            json_data["middle_name"],
            json_data["address"],
            json_data["phone"]
        )
    

    @property
    def student_id(self):
        return self._student_id

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = Student._validate_address(value)
        
    # Полная версия объекта
    def __str__(self):
        return (f"Студент #{self._student_id}\n"
                f"Фамилия: {self._last_name}\n"
                f"Имя: {self._first_name}\n"
                f"Отчество: {self._middle_name}\n"
                f"Адрес: {self._address}\n"
                f"Телефон: {self.phone}")

    # Краткая версия объекта
    def short_info(self):
        return f"{self._last_name} {self._first_name[0]}.{self._middle_name[0]}. ({self.phone})"

    # Сравнение объектов
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (self._student_id == other._student_id and
                self._last_name == other._last_name and
                self._first_name == other._first_name and
                self._middle_name == other._middle_name and
                self._address == other._address and
                self.phone == other.phone)