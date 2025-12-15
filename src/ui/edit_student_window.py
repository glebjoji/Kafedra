"""
Модуль с окном редактирования студента (View слоя MVC).
Только UI, вся логика в контроллере.
"""
import tkinter as tk
from tkinter import messagebox

class EditStudentWindow:
    
    def __init__(self, controller, student):
        self.controller = controller
        self.student = student
        
        self.root = tk.Toplevel()
        self.root.title(f"Редактировать студента #{student.student_id}")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg='#f8fbff')
        self.root.transient(controller.main_controller.main_view.root)
        self.root.grab_set()
        
        self.setup_ui()
        self.populate_fields()
    
    def setup_ui(self):
        header_frame = tk.Frame(self.root, bg='#f8fbff')
        header_frame.pack(fill=tk.X, pady=(20, 15))
        
        tk.Label(
            header_frame,
            text=f"Редактирование студента #{self.student.student_id}",
            font=('Arial', 16, 'bold'),
            bg='#f8fbff', fg='#2c3e50'
        ).pack()
        
        form_frame = tk.Frame(self.root, bg='#f8fbff')
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        self.entries = {}
        
        fields = [
            ("Фамилия:", "last_name"),
            ("Имя:", "first_name"),
            ("Отчество:", "middle_name"),
            ("Адрес:", "address"),
            ("Телефон:", "phone")
        ]
        
        for i, (label_text, field_name) in enumerate(fields):
            tk.Label(
                form_frame,
                text=label_text,
                font=('Arial', 11),
                bg='#f8fbff', fg='#2c3e50',
                anchor='w'
            ).grid(row=i, column=0, sticky='w', pady=8)

            entry = tk.Entry(
                form_frame,
                font=('Arial', 11),
                bg='#e8f4fd',
                relief='flat',
                width=30
            )
            entry.grid(row=i, column=1, sticky='ew', pady=8, padx=(10, 0))
            
            self.entries[field_name] = entry
        
        form_frame.columnconfigure(1, weight=1)
        
        # Кнопки управления
        btn_frame = tk.Frame(self.root, bg='#f8fbff')
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Сохранить",
            font=('Arial', 12, 'bold'),
            bg='#3498db', fg='white',
            relief='flat', padx=30, pady=8,
            cursor='hand2',
            command=lambda: self.controller.on_save_clicked()
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Отмена",
            font=('Arial', 12),
            bg='#e74c3c', fg='white',
            relief='flat', padx=30, pady=8,
            cursor='hand2',
            command=lambda: self.controller.on_cancel_clicked()
        ).pack(side=tk.LEFT, padx=5)
    
    def populate_fields(self):
        self.entries["last_name"].insert(0, self.student.last_name)
        self.entries["first_name"].insert(0, self.student.first_name)
        self.entries["middle_name"].insert(0, self.student.middle_name)
        self.entries["address"].insert(0, self.student.address)
        self.entries["phone"].insert(0, self.student.phone)
    
    def get_form_data(self):
        """
        Получить данные из формы
        :return: словарь с данными формы
        """
        data = {}
        for field_name, entry in self.entries.items():
            data[field_name] = entry.get().strip()
        return data
    
    def show_error(self, message):
        messagebox.showerror("Ошибка", message, parent=self.root)
    
    def show_success(self, message):
        messagebox.showinfo("Успех", message, parent=self.root)
    
    def close(self):
        self.root.destroy()