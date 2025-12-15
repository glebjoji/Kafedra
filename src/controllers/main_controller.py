"""
Модуль с контроллером главного окна MVC.
Вся логика через паттерн наблюдатель.
"""
from src.data.student_repl_json import Student_repl_json
from src.observer.repository_observer import RepositoryObserver
from src.ui.main_window import MainWindow
from src.ui.detail_window import DetailWindow
from src.controllers.add_student_controller import AddStudentController
from src.controllers.edit_student_controller import EditStudentController  

class MainController:
    
    def __init__(self):
        self.repo = Student_repl_json("students.json")
        self.observer = RepositoryObserver(self.repo)
        
        self.observer.subscribe(self._on_data_received)
        
        self.main_view = MainWindow(self)
        self.detail_view = None
        self.add_student_controller = None
        self.edit_student_controller = None  
        
        self.load_data()
    
    def _on_data_received(self, short_list):
        self.main_view.refresh_table(short_list)
    
    def load_data(self):
        short_list = self.observer.fetch_short_list(0, 20)
        self.observer.notify_data_loaded(short_list)
    
    def on_details_requested(self):
        selected_info = self.main_view.get_selected_item()
        
        if not selected_info:
            return
        
        student = self.observer.fetch_student_by_short_info(selected_info)
        
        if student:
            full_info = str(student)
        else:
            full_info = "Студент не найден"
        
        self.detail_view = DetailWindow(self, full_info)
    
    def on_add_student_requested(self):
        """Открытие окна добавления студента"""
        self.add_student_controller = AddStudentController(self)
    
    def on_edit_student_requested(self):  
        """Открытие окна редактирования студента"""
        selected_info = self.main_view.get_selected_item()
        
        if not selected_info:
            self.main_view.show_warning("Выберите студента для редактирования")
            return
        
        # полный объект студента
        student = self.observer.fetch_student_by_short_info(selected_info)
        
        if student:
            self.edit_student_controller = EditStudentController(self, student)
        else:
            self.main_view.show_error("Студент не найден")
    
    def run(self):
        self.main_view.run()