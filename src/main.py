from src.student import Student
from src.student_repl_json import Student_repl_json

    #Проверка для нового пункт 3
from src.student import Student
from src.student_repl_json import Student_repl_json

def main():
    repo = Student_repl_json("students.json")

    print("1. Добавление студентов")
    s1 = Student('{"student_id":0,"last_name":"Иванов","first_name":"Иван","middle_name":"Иванович","address":"Москва","phone":"+79111111111"}')
    s2 = Student('{"student_id":0,"last_name":"Петров","first_name":"Петр","middle_name":"Петрович","address":"Санкт-Петербург","phone":"+79222222222"}')

    repo.add_student(s1)
    repo.add_student(s2)

    print("Добавлено студентов:", repo.get_count())
    print()

    print("2. Список всех студентов")
    for st in repo.read_all():
        print(st.short_info())
    print()

    print("3. Получение по ID")
    found = repo.get_by_id(1)
    if found:
        print(found.short_info())
    print()

    print("4. Обновление студента с ID=2")
    new_s2 = Student('{"student_id":2,"last_name":"Сидоров","first_name":"Сидор","middle_name":"Сидорович","address":"Казань","phone":"+79333333333"}')
    repo.update_student(2, new_s2)
    print("После обновления:")
    for st in repo.read_all():
        print(st.short_info())
    print()

    print("5. Сортировка по фамилии")
    repo.sort_by_last_name()
    for st in repo.read_all():
        print(st.short_info())
    print()

    print("6. Удаление студента с ID=1")
    repo.delete_student(1)
    for st in repo.read_all():
        print(st.short_info())
    print()

    print("7. Постраничный вывод (k=0, n=1)")
    print(repo.get_k_n_short_list(0, 1))
    print()

    print("8. Количество студентов")
    print(repo.get_count())


if __name__ == "__main__":
    main()


        