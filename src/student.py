import phonenumbers
import re

class Student:

    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        self._student_id = student_id
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
        self._address = address
        self._phone = phone_string 

    @staticmethod
    def _validate_name_part(value: str, full_name: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{full_name} не может быть пустым.")

        if not re.fullmatch(r"[А-ЯЁ][а-яё]+", value):
            raise ValueError(f"{full_name} должно быть на кириллице, начинаться с заглавной буквы и содержать только буквы.")

        return value

    @staticmethod
    def _validate_last_name(last_name):
        return Student._validate_name_part(last_name, "Фамилия")

    @staticmethod
    def _validate_first_name(first_name):
        return Student._validate_name_part(first_name, "Имя")

    @staticmethod
    def _validate_middle_name(middle_name):
        return Student._validate_name_part(middle_name, "Отчество")

    @staticmethod
    def _validate_address(address):
        if not isinstance(address, str) or not address.strip():
            raise ValueError("Адрес должен быть непустой строкой.")

        # Требуем хотя бы одну букву кириллицы
        if not re.search(r"[А-Яа-яЁё]", address):
            raise ValueError("Адрес должен содержать хотя бы одну кириллическую букву.")

    @staticmethod
    def _validate_phone(phone_string):
        try:
            parsed_phone = phonenumbers.parse(phone_string, "RU")

            # Проверка для России
            if not phonenumbers.is_valid_number_for_region(parsed_phone, "RU"):
                raise ValueError("Некорректный номер телефона для Российского региона.")
            return parsed_phone
        except phonenumbers.NumberParseException:
            raise ValueError("Ошибка при разборе номера телефона. Проверьте формат.")
    

    @property
    def student_id(self):
        return self._student_id

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = Student._validate_last_name(value)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = Student._validate_first_name(value)

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = Student._validate_middle_name(value)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = Student._validate_address(value)
        
#Геттер для номера телефона возвращает форматированный номер
    @property
    def phone(self):
        return phonenumbers.format_number(self._phone, phonenumbers.PhoneNumberFormat.E164)
 
    @phone.setter
    def phone(self, value):
        self._phone = Student._validate_phone(value)