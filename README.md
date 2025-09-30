Тема: "Распределение учебной нагрузки"
Описание предметной области

Вы работаете в высшем учебном заведении и занимаетесь распределением нагрузки между преподавателями кафедры. В вашем распоряжении имеются сведения о преподавателях кафедры, включающие наряду с анкетными данными информацию об их ученой степени, занимаемой административной должности и стаже работы. Преподаватели вашей кафедры должны обеспечить проведение занятий по некоторым предметам. По каждому из них установлено определенное количество часов. В результате распределения нагрузки у вас должна получиться информация следующего рода: «Такой-то преподаватель проводит занятия по такому-то предмету с такой-то группой».

Задание ЛР1.
1. Выбрать тему, построить ER модель предметной области - 3-4 таблицы в 3НФ.
<img width="1248" height="439" alt="image" src="https://github.com/user-attachments/assets/5f4b3928-d5e2-4187-9dc2-4fafbe0f78e0" />
2. Выбрать независимую сущность с наибольшим числом полей (клиент, организация, студент, пользователь и тд) - дальше ЛР1 - ЛР4 работа только с этой сущностью.

Student
3. Построить полный класс этой сущности. Обеспечить инкапсуляцию ВСЕХ полей.
```
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
```
4. Сделать методы класса (статические) валидации всех необходимых полей. Сделать так, чтобы существование объекта с неразрешёнными полями было невозможно.
   ```
   @staticmethod
    def _validate_last_name(last_name):
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("Фамилия не может быть пустой.")

        # Кириллица, первая буква заглавная, остальные строчные
        if not re.fullmatch(r"[А-ЯЁ][а-яё]+", last_name):
            raise ValueError("Фамилия должна быть на кириллице, начинаться с заглавной буквы и содержать только буквы.")

    @staticmethod
    def _validate_first_name(first_name):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("Имя не может быть пустым.")

        if not re.fullmatch(r"[А-ЯЁ][а-яё]+", first_name):
            raise ValueError("Имя должно быть на кириллице, начинаться с заглавной буквы и содержать только буквы.")

    @staticmethod
    def _validate_middle_name(middle_name):
        if not isinstance(middle_name, str) or not middle_name.strip():
            raise ValueError("Отчество не может быть пустым.")

        if not re.fullmatch(r"[А-ЯЁ][а-яё]+", middle_name):
            raise ValueError("Отчество должно быть на кириллице, начинаться с заглавной буквы и содержать только буквы.")

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
   ```
   5. Убрать повтор кода из пункта 4.
      
   ```
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
   ```
   6. Обеспечить перегрузку конcтруктора для нетривиальных примеров (строка, JSON и тд).
      
   ```
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
   ```
   7. 
```
from .student import Student
import json

if __name__ == "__main__":
        s1 = Student(1, "Иванов", "Иван", "Иванович", "г. Москва, ул. Ленина, д. 10", "+79123456789")
        print(f"Объект создан: {s1}")
        print(f"Полное представление: {repr(s1)}")

        s2 = Student(2, "Иванов","Петр","Сергеевич","г. Москва, ул. Ленина, д. 5","+7 999 123 45 67" )

        print("Полная версия:")
        print(s1)
        print("\nКраткая версия:")
        print(s1.short_info())

        print("\nСравнение объектов:")
        print("s1 == s2 ?", s1 == s2)
```
8.Создать класс, содержащий краткую версию данных исходного класса (например Фамилия Инициалы, только один контакт, ИНН ОГРН без адреса, без контактных лиц и тд).
  ```
   from src.student import Student


class StudentSummary:

    def __init__(self, student: Student):
        self._student = student  

    @property
    def last_name(self):
        return self._student.last_name

    @property
    def phone(self):
        return self._student.phone

    def __str__(self):
        return f"{self.last_name} {self.phone}"
```
9.
```
import phonenumbers
import re


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
        return phonenumbers.format_number(self._phone, phonenumbers.PhoneNumberFormat.E164)
 
    @phone.setter
    def phone(self, value):
        self._phone = StudentBase._validate_phone(value)
```
10.
<img width="2439" height="3840" alt="image" src="https://github.com/user-attachments/assets/60c2e160-b5e5-480d-a122-005b2164fd0e" />
