"""
Модуль с базовым классом StudentBase.
Содержит общие данные студента: ФИО и телефон с валидацией.
"""

import re

import phonenumbers


class StudentBase:
    # Класс с общими данными ФИО и телефон.

    def __init__(self, student_id, last_name, first_name, middle_name, phone_string):
        self._student_id = student_id
        self._last_name = self._validate_name_part(last_name, "Фамилия")
        self._first_name = self._validate_name_part(first_name, "Имя")
        self._middle_name = self._validate_name_part(middle_name, "Отчество")
        self._phone = self._validate_phone(phone_string)

    @staticmethod
    def _validate_name_part(value: str, full_name: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{full_name} не может быть пустым.")
        if not re.fullmatch(r"[А-ЯЁ][а-яё]+", value):
            raise ValueError(
                f"{full_name} должно быть на кириллице, "
                f"начинаться с заглавной буквы и содержать только буквы."
            )
        return value

    @staticmethod
    def _validate_last_name(last_name):
        return StudentBase._validate_name_part(last_name, "Фамилия")

    @staticmethod
    def _validate_first_name(first_name):
        return StudentBase._validate_name_part(first_name, "Имя")

    @staticmethod
    def _validate_middle_name(middle_name):
        return StudentBase._validate_name_part(middle_name, "Отчество")

    @staticmethod
    def _validate_phone(phone_string):
        try:
            parsed_phone = phonenumbers.parse(phone_string, "RU")
            if not phonenumbers.is_valid_number_for_region(parsed_phone, "RU"):
                raise ValueError("Некорректный номер телефона для Российского региона.")
            return parsed_phone
        except phonenumbers.NumberParseException:
            raise ValueError("Ошибка при разборе номера телефона. Проверьте формат.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = StudentBase._validate_last_name(value)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = StudentBase._validate_first_name(value)

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = StudentBase._validate_middle_name(value)

    @property
    def phone(self):
        return phonenumbers.format_number(
            self._phone, phonenumbers.PhoneNumberFormat.E164
        )

    @phone.setter
    def phone(self, value):
        self._phone = StudentBase._validate_phone(value)
