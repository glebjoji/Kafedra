from src.student_repl_json import Student_repl_json
#from src.student_summary import StudentSummary
from src.student import Student


# if __name__ == "__main__":
#         s1 = Student("1, Иванов, Иван, Иванович, г. Москва, ул. Ленина, д. 10, +79123456789")
#         print(f"Объект создан: {s1}")
#         print("\nВывод номера студента:")
#         s1.phone = "+79999999999"
#         print(s1.phone)
#         print(f"Полное представление: {repr(s1)}")

#         s2 = Student(2, "Иванов","Петр","Сергеевич","г. Москва, ул. Ленина, д. 5","+7 999 123 45 67" )

#         summary = StudentSummary(s2)

#         s3 = Student('{"student_id":3,"last_name":"Сергеев","first_name":"Пётр","middle_name":"Иванович","address":"г. Москва, ул. Ленина, д. 10","phone":"+79123456799"}')

#         print("Полная версия:")
#         print(s1)
#         print("\nКраткая версия:")
#         print(s1.short_info())

#         print("\nУпрощенная версия из summary:")
#         print(summary)

#         print("\nпроверка вывода json:")
#         print(s3)

#         print("\nСравнение объектов:")
#         print("s1 == s2 ?", s1 == s2)



    #Проверка для нового пункт 1

repo = Student_repl_json("students.json")

print("\n Работа с Student_rep_json")
    # (a) Чтение всех значений (если файл есть)
print("\n(a) Содержимое файла (до изменений):")
all_before = repo.read_all()
for st in all_before:
        print("-", st.short_info())

    # (f) Добавление новых студентов
print("\n(f) Добавляем студентов:")
new1 = Student(0, "Петров", "Сергей", "Андреевич", "г. Санкт-Петербург, ул. Невская, д. 15", "+79998887766")
new2 = Student(0, "Сидоров", "Дмитрий", "Иванович", "г. Екатеринбург, ул. Ленина, д. 25", "+79991112233")

id1 = repo.add_student(new1)
id2 = repo.add_student(new2)
print(f"Добавлены с ID: {id1}, {id2}")

    # (b) Запись всех значений уже выполнена при добавлении, проверим (a) снова
print("\n(a) Содержимое файла (после добавления):")
all_after = repo.read_all()
for st in all_after:
        print("-", st.short_info())

    # (c) Получить по ID
print("\n(c) Получаем студента по ID:")
found = repo.get_by_id(id1)
print(found)

    # (d) Пагинация 
print("\n(d) Пагинация (первые 2 студента):")
for info in repo.get_k_n_short_list(0, 2):
        print(info)

    # (e) Сортировка по фамилии
print("\n(e) Сортировка по фамилии:")
repo.sort_by_last_name()
for st in repo.read_all():
        print("-", st.short_info())

    # (g) Замена студента по ID
print("\n(g) Замена студента:")
updated = Student(0, "Николаев", "Антон", "Олегович", "г. Казань, ул. Пушкина, д. 7", "+79990001122")
if repo.update_student(id2, updated):
        print(f"Студент с ID {id2} обновлён.")
else:
        print(f"Студент с ID {id2} не найден.")

    # результат замены
for st in repo.read_all():
        print("-", st.short_info())

    # (h) Удалить студента
print("\n(h) Удаление студента:")
if repo.delete_student(id1):
        print(f"Студент с ID {id1} удалён.")
else:
        print(f"Студент с ID {id1} не найден.")

print("Список после удаления:")
for st in repo.read_all():
        print("-", st.short_info())

    # (i) Получить количество студентов
print("\n(i) Общее количество студентов:", repo.get_count())


        