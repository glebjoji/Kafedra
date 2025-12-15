"""
Модуль с контроллером окна редактирования студента.
Вся логика валидации и обновления здесь.
"""

from src.core.student import Student
from src.ui.edit_student_window import EditStudentWindow

class EditStudentController:
    
    def __init__(self, main_controller, student):
        """
        Инициализация контроллера редактирования
        :param main_controller: ссылка на главный контроллер
        :param student: объект Student для редактирования
        """
        self.main_controller = main_controller
        self.observer = main_controller.observer
        self.student = student  # Сохраняем оригинальный объект студента
        self.view = EditStudentWindow(self, student)
    
    def on_save_clicked(self):
        """Обработка нажатия кнопки Сохранить"""
        form_data = self.view.get_form_data()
        
        try:
            # Создаем обновленный объект студента
            updated_student = Student(
                self.student.student_id,  # Сохраняем оригинальный ID
                form_data["last_name"],
                form_data["first_name"],
                form_data["middle_name"],
                form_data["address"],
                form_data["phone"]
            )
        except ValueError as e:
            self.view.show_error(f"Ошибка валидации данных: {e}")
            return
        
        # Обновление через репозиторий
        try:
            success = self._update_student(updated_student)
            
            if success:
                self.view.show_success(f"Студент #{self.student.student_id} успешно обновлен")
                
                # Обновляем главное окно
                self.main_controller.load_data()
                
                # Закрываем окно редактирования
                self.view.close()
            else:
                self.view.show_error("Не удалось обновить запись студента")
        
        except Exception as e:
            self.view.show_error(f"Ошибка при сохранении: {e}")
    
    def on_cancel_clicked(self):
        """Обработка нажатия кнопки Отмена"""
        self.view.close()
    
    def _update_student(self, student):
        """
        Обновление студента через репозиторий
        :param student: обновленный объект Student
        :return: True если успешно, False иначе
        """
        return self.observer.repo.update_student(student.student_id, student)