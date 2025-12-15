"""
Модуль с универсальным окном формы студента (View слоя MVC).
Используется как для добавления, так и для редактирования студента.
Только UI, вся логика в контроллерах.
"""
import tkinter as tk
from tkinter import messagebox


class StudentFormWindow:

    def __init__(self, controller, title: str, student=None):
        self.controller = controller
        self.student = student
        self.is_edit_mode = student is not None
        
        self.root = tk.Toplevel()
        self.root.title(title)
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg='#f8fbff')
        self.root.transient(controller.main_controller.main_view.root)
        self.root.grab_set()
        
        self.setup_ui(title)
    
    def setup_ui(self, title: str):
        header_frame = tk.Frame(self.root, bg='#f8fbff')
        header_frame.pack(fill=tk.X, pady=(20, 15))
        
        tk.Label(
            header_frame,
            text=title,
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

        btn_frame = tk.Frame(self.root, bg='#f8fbff')
        btn_frame.pack(pady=20)
        
        save_btn_color = '#3498db' if self.is_edit_mode else '#27ae60'
        
        tk.Button(
            btn_frame,
            text="Сохранить",
            font=('Arial', 12, 'bold'),
            bg=save_btn_color, fg='white',
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
    
    def set_field_value(self, field_name: str, value: str):
        if field_name in self.entries:
            entry = self.entries[field_name]
            entry.delete(0, tk.END)
            entry.insert(0, value)
            entry.config(fg='black')  
    
    def set_placeholder(self, field_name: str, placeholder: str):
        if field_name in self.entries:
            entry = self.entries[field_name]
            entry.insert(0, placeholder)
            entry.config(fg='grey')
            
            # обработчики для placeholder
            entry.bind(
                '<FocusIn>',
                lambda e, ent=entry, ph=placeholder: self._on_focus_in(ent, ph)
            )
            entry.bind(
                '<FocusOut>',
                lambda e, ent=entry, ph=placeholder: self._on_focus_out(ent, ph)
            )
    
    def _on_focus_in(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')
    
    def _on_focus_out(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='grey')
    
    def get_form_data(self) -> dict:
        data = {}
        for field_name, entry in self.entries.items():
            data[field_name] = entry.get().strip()
        return data
    
    def show_error(self, message: str):
        messagebox.showerror("Ошибка", message, parent=self.root)
    
    def show_success(self, message: str):
        messagebox.showinfo("Успех", message, parent=self.root)
    
    def close(self):
        self.root.destroy()