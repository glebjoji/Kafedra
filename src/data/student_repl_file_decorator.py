"""
Модуль с декоратором для файловых репозиториев студентов.
Позволяет применять фильтры и сортировку при вызове get_k_n_short_list и get_count.
"""


class Student_repl_file_decorator:
    # param wrapped_repo: Student_repl_json или Student_repl_yaml
    # param reverse:True- по убыванию, False- по возрастанию)

    def __init__(self, wrapped_repo, filter_func=None, sort_key=None, reverse=False):
        self.wrapped_repo = wrapped_repo
        self.filter_func = filter_func
        self.sort_key = sort_key
        self.reverse = reverse

    def _apply_filter_and_sort(self, students):
        # Применяет фильтрацию и сортировку к списку студентов
        result = students
        if self.filter_func:
            result = list(filter(self.filter_func, result))
        if self.sort_key:
            result.sort(key=self.sort_key, reverse=self.reverse)
        return result

    def get_k_n_short_list(self, k, n):
        students = self.wrapped_repo.read_all()
        students = self._apply_filter_and_sort(students)

        start = (n - 1) * k
        end = start + k
        selected = students[start:end]
        return [s.short_info() for s in selected]

    def get_count(self):
        students = self.wrapped_repo.read_all()
        students = self._apply_filter_and_sort(students)
        return len(students)
