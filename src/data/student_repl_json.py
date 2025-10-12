import json
import os
from src.core.student import Student
from src.data.student_repl_base import Student_repl_base


class Student_repl_json(Student_repl_base):
    def __init__(self, filename: str):
        super().__init__(filename)
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                #Запаковка
                json.dump([], f, ensure_ascii=False, indent=4)

    def read_all(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            #Распаковка
        return [Student(json.dumps(obj, ensure_ascii=False)) for obj in data]

    def write_all(self, students):
        data = []
        for s in students:
            data.append({
                "student_id": s.student_id,
                "last_name": s.last_name,
                "first_name": s.first_name,
                "middle_name": s.middle_name,
                "address": s.address,
                "phone": s.phone
            })
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
