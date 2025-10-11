import json
import os
from src.student import Student


class Student_repl_json:
    def __init__(self, filename: str):
        self.filename = filename
        # Если файла нет — создаём пустой JSON
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    
    # a. Чтение всех значений из файла
    def read_all(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Преобразуем словари в объекты Student
        return [Student(json.dumps(obj, ensure_ascii=False)) for obj in data]


    # b. Запись всех значений в файл
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


    # c. Получить объект по ID
    def get_by_id(self, student_id: int):
        students = self.read_all()
        for s in students:
            if s.student_id == student_id:
                return s
        return None


    #постраничный вывод
    def get_k_n_short_list(self, k: int, n: int):

        #Получить n элементов, начиная с позиции k (нумерация с 0)

        students = self.read_all()
        selected = students[k:k + n]
        return [s.short_info() for s in selected]


    # e. Сортировать элементы по выбранному полю 
    def sort_by_last_name(self):
        students = self.read_all()
        students.sort(key=lambda s: s.last_name)
        self.write_all(students)


    # f. Добавить объект в список (с новым ID)
    def add_student(self, student: Student):
        students = self.read_all()
        # Новый ID — на 1 больше максимального
        new_id = max([s.student_id for s in students], default=0) + 1
        student._student_id = new_id
        students.append(student)
        self.write_all(students)
        return new_id

    # g. Заменить элемент по ID
    def update_student(self, student_id: int, new_student: Student):
        students = self.read_all()
        for i, s in enumerate(students):
            if s.student_id == student_id:
                new_student._student_id = student_id
                students[i] = new_student
                self.write_all(students)
                return True
        return False


    # h. Удалить элемент по ID
    def delete_student(self, student_id: int):
        students = self.read_all()
        new_students = [s for s in students if s.student_id != student_id]
        self.write_all(new_students)
        return len(new_students) < len(students)


    # i. Получить количество элементов
    def get_count(self):
        students = self.read_all()
        return len(students)
