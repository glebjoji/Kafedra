"""
Главный модуль проекта.
Создаёт репозиторий студентов из базы данных и выводит информацию о студентах.
"""

from src.data.student_repl_file_decorator import Student_repl_file_decorator
from src.data.student_repl_json import Student_repl_json

repo = Student_repl_json("students.json")

decorator = Student_repl_file_decorator(
    repo,
    filter_func=lambda s: "Москва" in s.address,
    sort_key=lambda s: s.last_name,
    reverse=True,
)

print("Студенты из Москвы (по фамилии, от Я к А):")
for s in decorator.get_k_n_short_list(5, 1):
    print(s)

print(f"Количество студентов из Москвы: {decorator.get_count()}")
