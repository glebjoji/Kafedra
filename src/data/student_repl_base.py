"""
Модуль с абстрактным базовым классом Student_repl_base.
Определяет общие методы для всех репозиториев студентов (файловых и баз данных).
"""

from abc import ABC, abstractmethod
from src.core.student import Student


class Student_repl_base(ABC):

    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def write_all(self, students):
        pass

    def get_by_id(self, student_id: int):
        students = self.read_all()
        for s in students:
            if s.student_id == student_id:
                return s
        return None

    def get_k_n_short_list(self, k: int, n: int):
        students = self.read_all()
        selected = students[k : k + n]
        return [s.short_info() for s in selected]

    def sort_by_last_name(self):
        students = self.read_all()
        students.sort(key=lambda s: s.last_name)
        self.write_all(students)

    def add_student(self, student: Student):
        students = self.read_all()
        new_id = max([s.student_id for s in students], default=0) + 1
        student._student_id = new_id
        students.append(student)
        self.write_all(students)
        return new_id

    def update_student(self, student_id: int, new_student: Student):
        students = self.read_all()
        for i, s in enumerate(students):
            if s.student_id == student_id:
                new_student._student_id = student_id
                students[i] = new_student
                self.write_all(students)
                return True
        return False

    def delete_student(self, student_id: int):
        students = self.read_all()
        new_students = [s for s in students if s.student_id != student_id]
        self.write_all(new_students)
        return len(new_students) < len(students)

    def get_count(self):
        return len(self.read_all())
