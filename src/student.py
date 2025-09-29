import phonenumbers

class Student:
    def __init__(self, student_id, last_name, first_name, middle_name, address, phone_string):
        self._student_id = student_id
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
        self._address = address
        self._phone = phone_string # пока просто строка, валидация будет в следующем пункте
#геттеры и сеттеры
    @property
    def student_id(self):
        return self._student_id

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        
#Геттер для номера телефона возвращает форматированный номер
    @property
    def phone(self):
        return phonenumbers.format_number(self._phone, phonenumbers.PhoneNumberFormat.E164)

#Сеттер для номера телефона с валидацией 
    @phone.setter
    def phone(self, value):
        self._phone = Student._validate_phone(value)