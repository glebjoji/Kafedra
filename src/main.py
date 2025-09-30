from student_summary import StudentSummary
from .student import Student
import json

if __name__ == "__main__":
        s1 = Student(1, "Иванов", "Иван", "Иванович", "г. Москва, ул. Ленина, д. 10", "+79123456789")
        print(f"Объект создан: {s1}")
        print(f"Полное представление: {repr(s1)}")

        s2 = Student(2, "Иванов","Петр","Сергеевич","г. Москва, ул. Ленина, д. 5","+7 999 123 45 67" )

        summary = StudentSummary(s2)

        print("Полная версия:")
        print(s1)
        print("\nКраткая версия:")
        print(s1.short_info())

        print(summary)

        print("\nСравнение объектов:")
        print("s1 == s2 ?", s1 == s2)