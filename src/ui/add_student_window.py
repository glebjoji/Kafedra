"""
Модуль с окном добавления студента (View слоя MVC).
Только UI, вся логика в контроллере.
"""

import tkinter as tk
from tkinter import messagebox


class AddStudentWindow:
    
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Toplevel()
        self.root.title("Добавить студента")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg='#f8fbff')
        self.root.transient(controller.main_controller.main_view.root)
        self.root.grab_set()
        
        self.setup_ui()
    
    def setup_ui(self):
        header_frame = tk.Frame(self.root, bg='#f8fbff')
        header_frame.pack(fill=tk.X, pady=(20, 15))
        
        tk.Label(
            header_frame,
            text="Добавить нового студента",
            font=('Arial', 16, 'bold'),
            bg='#f8fbff', fg='#2c3e50'
        ).pack()
        
        form_frame = tk.Frame(self.root, bg='#f8fbff')
        form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=10)
        
        self.entries = {}
        
        fields = [
            ("Фамилия:", "last_name", "Иванов"),
            ("Имя:", "first_name", "Иван"),
            ("Отчество:", "middle_name", "Иванович"),
            ("Адрес:", "address", "Москва, ул. Ленина, д. 1"),
            ("Телефон:", "phone", "+79161234567")
        ]
        
        for i, (label_text, field_name, placeholder) in enumerate(fields):
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
            entry.insert(0, placeholder)
            entry.config(fg='grey')
            
            entry.bind('<FocusIn>', lambda e, ent=entry, ph=placeholder: self._on_focus_in(ent, ph))
            entry.bind('<FocusOut>', lambda e, ent=entry, ph=placeholder: self._on_focus_out(ent, ph))
            
            self.entries[field_name] = entry
        
        form_frame.columnconfigure(1, weight=1)
        
        btn_frame = tk.Frame(self.root, bg='#f8fbff')
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Сохранить",
            font=('Arial', 12, 'bold'),
            bg='#27ae60', fg='white',
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
    
    def _on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')
    
    def _on_focus_out(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='grey')
    
    def get_form_data(self):
        #Получить данные из формы
        data = {}
        placeholders = {
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "address": "Москва, ул. Ленина, д. 1",
            "phone": "+79161234567"
        }
        
        for field_name, entry in self.entries.items():
            value = entry.get()
            if value == placeholders.get(field_name):
                data[field_name] = ""
            else:
                data[field_name] = value.strip()
        
        return data
    
    def show_error(self, message):
        messagebox.showerror("Ошибка", message, parent=self.root)
    
    def show_success(self, message):
        messagebox.showinfo("Успех", message, parent=self.root)
    
    def close(self):
        self.root.destroy()
