from src.student import Student
from src.student_repl_db import Student_repl_db


def main():
    repo = Student_repl_db(
        db_name="DB",
        user="postgres",
        password="1234",
        host="localhost",
        port=5432
    )

    print("\nКоличество студентов:", repo.get_count())

    new_student = Student(
        0, "Иванова", "Ивана", "Ивановна",
        "г. Москва, ул. Ленина, д. 11",
        "+79981234567"
    )
    new_id = repo.add_student(new_student)
    print("\nДобавлен студент с ID:", new_id)

    student = repo.get_by_id(new_id)
    print("\nНайден:", student)

    student._address = "г. Москва, ул. Новая, д. 5"
    repo.update_student(new_id, student)
    print("\nАдрес обновлён!", student._address)

    print("\nСтраница 1 (по 1 записи):")
    for s in repo.get_k_n_short_list(k=1, n=1):
        print(s)

    repo.delete_student(new_id)
    print(f"Студент с ID={new_id} удалён.")

    print("\nВсего студентов:", repo.get_count())


if __name__ == "__main__":
    main()
