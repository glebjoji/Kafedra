"""
Модуль с контроллером окна добавления студента.
Логика заполнения формы пустыми полями с placeholder.
"""
from src.core.student import Student
from src.ui.student_form_window import StudentFormWindow


class AddStudentController:
    
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.observer = main_controller.observer

        self.view = StudentFormWindow(
            controller=self,
            title="Добавить нового студента",
            student=None
        )

        self._setup_placeholders()
    
    def _setup_placeholders(self):
        placeholders = {
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "address": "Москва, ул. Ленина, д. 1",
            "phone": "+79161234567"
        }
        
        for field_name, placeholder in placeholders.items():
            self.view.set_placeholder(field_name, placeholder)
    
    def populate_form_fields(self):
        pass  
    
    def on_save_clicked(self):
        form_data = self.view.get_form_data()
        
        placeholders = {
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "address": "Москва, ул. Ленина, д. 1",
            "phone": "+79161234567"
        }
        
        cleaned_data = {}
        for field_name, value in form_data.items():
            if value == placeholders.get(field_name):
                cleaned_data[field_name] = ""
            else:
                cleaned_data[field_name] = value
        
        try:
            student = Student(
                1,  # ID будет установлен репозиторием
                cleaned_data["last_name"],
                cleaned_data["first_name"],
                cleaned_data["middle_name"],
                cleaned_data["address"],
                cleaned_data["phone"]
            )
        except ValueError as e:
            self.view.show_error(f"Ошибка данных: {e}")
            return
        
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