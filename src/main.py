from src.student_summary import StudentSummary
from src.student import Student

if __name__ == "__main__":
        s1 = Student("1, Иванов, Иван, Иванович, г. Москва, ул. Ленина, д. 10, +79123456789")
        print(f"Объект создан: {s1}")
        print("\nВывод номера студента:")
        s1.phone = "+79999999999"
        print(s1.phone)
        print(f"Полное представление: {repr(s1)}")

        s2 = Student(2, "Иванов","Петр","Сергеевич","г. Москва, ул. Ленина, д. 5","+7 999 123 45 67" )

        summary = StudentSummary(s2)

        s3 = Student('{"student_id":3,"last_name":"Сергеев","first_name":"Пётр","middle_name":"Иванович","address":"г. Москва, ул. Ленина, д. 10","phone":"+79123456799"}')

        print("Полная версия:")
        print(s1)
        print("\nКраткая версия:")
        print(s1.short_info())

        print("\nУпрощенная версия из summary:")
        print(summary)

        print("\nпроверка вывода json:")
        print(s3)

        print("\nСравнение объектов:")
        print("s1 == s2 ?", s1 == s2)

        arr1 = [1,2]
        arr2 = [1,2]
        print(arr1==arr2)

        