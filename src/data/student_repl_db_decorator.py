from src.data.student_repl_base import Student_repl_base


class Student_repl_db_decorator(Student_repl_base):

    def __init__(
        self,
        wrapped_repo: Student_repl_base,
        filter_func=None,
        sort_key=None,
        reverse=False,
    ):

        # param wrapped_repo: репозиторий
        # param filter_func: фильр по чему-либо, задается например
        # filter_func = lambda s: s.last_name.startswith("А")
        # filter_func = lambda s: "е" in s.first_name.lower()
        # param sort_key: сортировка, например sort_key = lambda s: s.last_name
        # param reverse: порядок сортировки (True = по убываниб и наоборот)

        super().__init__(filename=None)
        self._repo = wrapped_repo
        self._filter_func = filter_func
        self._sort_key = sort_key
        self._reverse = reverse

    def read_all(self):
        return self._repo.read_all()

    def write_all(self, students):
        self._repo.write_all(students)

    def get_k_n_short_list(self, k: int, n: int):
        # добавление фильтра и сортировки
        students = self._repo.read_all()

        if self._filter_func:
            students = list(filter(self._filter_func, students))

        if self._sort_key:
            students.sort(key=self._sort_key, reverse=self._reverse)

        start_index = (n - 1) * k
        end_index = start_index + k
        return [s.short_info() for s in students[start_index:end_index]]

    def get_count(self):
        # возвращает количество студентов с учётом фильтра
        students = self._repo.read_all()
        if self._filter_func:
            students = list(filter(self._filter_func, students))
        return len(students)
