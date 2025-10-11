from src.student_repl_db import Student_repl_db

def main():
    repo = Student_repl_db()

    print(f"Всего студентов: {repo.get_count()}")

    first = repo.get_by_id(10)
    if first:
        print("Первый студент:")
        print(first)
    else:
        print("Студент с ID=1 не найден.")

    print("\nПервые 5 студентов:")
    for s in repo.get_k_n_short_list(5, 1):
        print(s.short_info())


if __name__ == "__main__":
    main()
