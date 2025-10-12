"""
Модуль с классом Student, наследуемым от StudentBase.
Поддерживает создание студента из:
  1) отдельных аргументов,
  2) CSV строки,
  3) JSON строки.
"""

import json
import re

from src.core.student_base import StudentBase


class Student(StudentBase):
    def __init__(self, *args):
        # Конструктор поддерживает:
        # 1) Student(id, last, first, middle, address, phone)
        # 2) Student("id, last, first, middle, address, phone")
        # 3) Student('{"student_id":, "last_name":, "first_name":, "middle_name":, "address":, "phone":}')

        # В1: обычный вызов 6 аргументов
        if len(args) == 6:
            student_id, last_name, first_name, middle_name, address, phone = args
            super().__init__(int(student_id), last_name, first_name, middle_name, phone)
            self._address = self._validate_address(address)
            return

        # В2 и В3: передана одна строка
        if len(args) == 1 and isinstance(args[0], str):
            data = args[0].strip()

            # JSON
            if data.startswith("{") and data.endswith("}"):
                try:
                    obj = json.loads(data)
                    super().__init__(
                        int(obj["student_id"]),
                        obj["last_name"],
                        obj["first_name"],
                        obj["middle_name"],
                        obj["phone"],
                    )
                    self._address = self._validate_address(obj["address"])
                    return
                except (json.JSONDecodeError, KeyError) as e:
                    raise ValueError(f"Ошибка разбора JSON: {e}")

            # CSV-строка
            parts = [p.strip() for p in data.split(",")]
            if len(parts) < 6:
                raise ValueError("Недостаточно данных. Ожидается минимум 6 полей.")

            # Первые 4 — фиксированные
            student_id = parts[0]
            last_name = parts[1]
            first_name = parts[2]
            middle_name = parts[3]

            # Всё между 4-м и предпоследним — это адрес
            address = ", ".join(parts[4:-1])
            phone = parts[-1]

            super().__init__(int(student_id), last_name, first_name, middle_name, phone)
            self._address = self._validate_address(address)
            return

    @staticmethod
    def _validate_address(address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Адрес должен быть непустой строкой.")
        if not re.search(r"[А-Яа-яЁё]+", address):
            raise ValueError("Адрес должен содержать хотя бы одну кириллическую букву.")
        return address

    @property
    def student_id(self):
        return self._student_id

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = Student._validate_address(value)

    # Строковое представление
    def __str__(self):
        return (
            f"Студент #{self._student_id}\n"
            f"Фамилия: {self._last_name}\n"
            f"Имя: {self._first_name}\n"
            f"Отчество: {self._middle_name}\n"
            f"Адрес: {self._address}\n"
            f"Телефон: {self.phone}"
        )

    def short_info(self):
        return f"{self._last_name} {self._first_name[0]}.{self._middle_name[0]}. ({self.phone})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (
            self._first_name == other._first_name
            and self._middle_name == other._middle_name
            and self.phone == other.phone
        )
