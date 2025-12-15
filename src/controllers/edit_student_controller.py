"""
Модуль с контроллером окна редактирования студента.
Логика заполнения формы существующими данными студента.
"""
from src.core.student import Student
from src.ui.student_form_window import StudentFormWindow


class EditStudentController:
    
    def __init__(self, main_controller, student):
        self.main_controller = main_controller
        self.observer = main_controller.observer
        self.student = student

        self.view = StudentFormWindow(
            controller=self,
            title=f"Редактирование студента #{student.student_id}",
            student=student
        )
  
        self.populate_form_fields()
    
    def populate_form_fields(self):
        self.view.set_field_value("last_name", self.student.last_name)
        self.view.set_field_value("first_name", self.student.first_name)
        self.view.set_field_value("middle_name", self.student.middle_name)
        self.view.set_field_value("address", self.student.address)
        self.view.set_field_value("phone", self.student.phone)
    
    def on_save_clicked(self):
        form_data = self.view.get_form_data()
        
        try:
            updated_student = Student(
                self.student.student_id,  
                form_data["last_name"],
                form_data["first_name"],
                form_data["middle_name"],
                form_data["address"],
                form_data["phone"]
            )
        except ValueError as e:
            self.view.show_error(f"Ошибка валидации данных: {e}")
            return
        
        try:
            success = self._update_student(updated_student)
            
            if success:
                self.view.show_success(
                    f"Студент #{self.student.student_id} успешно обновлен"
                )
                
                self.main_controller.load_data()
                
                self.view.close()
            else:
                self.view.show_error("Не удалось обновить запись студента")
        
        except Exception as e:
            self.view.show_error(f"Ошибка при сохранении: {e}")
    
    def on_cancel_clicked(self):
        self.view.close()
    
    def _update_student(self, student):
        return self.observer.repo.update_student(student.student_id, student)