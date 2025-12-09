"""
Модуль с контроллером окна добавления студента (отдельный контроллер).
Вся логика валидации и сохранения здесь.
"""

from src.core.student import Student
from src.ui.add_student_window import AddStudentWindow


class AddStudentController:
    
    def __init__(self, main_controller):
        self.main_controller = main_controller 
        self.observer = main_controller.observer  
        self.view = AddStudentWindow(self)
    
    def on_save_clicked(self):
        form_data = self.view.get_form_data()
        
        try:
            student = Student(
                1,  # ID будет установлен репозиторием
                form_data["last_name"],
                form_data["first_name"],
                form_data["middle_name"],
                form_data["address"],
                form_data["phone"]
            )
        except ValueError as e:
            self.view.show_error(f"Ошибка данных: {e}")
            return
        
        #Сохранение через наблюдателя
        try:
            new_id = self._save_student(student)
            self.view.show_success(f"Студент добавлен с ID: {new_id}")

            self.main_controller.load_data()
            
            self.view.close()
        
        except Exception as e:
            self.view.show_error(f"Ошибка сохранения: {e}")
    
    def on_cancel_clicked(self):
        self.view.close()
    
    def _save_student(self, student):
        return self.observer.repo.add_student(student)
