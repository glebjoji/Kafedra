from src.data.student_repl_db import Student_repl_db
from src.data.student_repl_db_decorator import Student_repl_db_decorator

def main():
    base_repo = Student_repl_db()

    filter_func = lambda s: s.last_name.startswith("И")

    sort_key = lambda s: s.first_name

    # декорация репозитория
    decorated_repo = Student_repl_db_decorator(
        base_repo,
        filter_func=filter_func,
        sort_key=sort_key,
        reverse=False
    )

    print(f"Всего студентов после фильтрации: {decorated_repo.get_count()}\n")

    print("Первые 5 студентов (фильтр + сортировка):")
    for s in decorated_repo.get_k_n_short_list(5, 1):
        print(s)


if __name__ == "__main__":
    main()
