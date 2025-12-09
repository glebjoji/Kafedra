import os

import yaml

from src.core.student import Student
from src.data.student_repl_base import Student_repl_base


class Student_repl_yaml(Student_repl_base):
    def __init__(self, filename: str):
        super().__init__(filename)
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                yaml.dump([], f, allow_unicode=True)

    def read_all(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
        return [
            Student(
                item["student_id"],
                item["last_name"],
                item["first_name"],
                item["middle_name"],
                item["address"],
                item["phone"],
            )
            for item in data
        ]

    def write_all(self, students):
        data = []
        for s in students:
            data.append(
                {
                    "student_id": s.student_id,
                    "last_name": s.last_name,
                    "first_name": s.first_name,
                    "middle_name": s.middle_name,
                    "address": s.address,
                    "phone": s.phone,
                }
            )
        with open(self.filename, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
