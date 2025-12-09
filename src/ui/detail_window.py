"""
Модуль с окном подробной информации о студенте (View слоя MVC).
"""

import tkinter as tk
from tkinter import scrolledtext

class DetailWindow:
    
    def __init__(self, controller, student_info: str):
        self.controller = controller
        self.root = tk.Toplevel()
        self.root.title("Подробности студента")
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        self.root.configure(bg='#f8fbff')
        self.root.transient(controller.main_view.root)
        self.root.grab_set()
        
        self.setup_ui(student_info)
    
    def setup_ui(self, student_info: str):
        header_frame = tk.Frame(self.root, bg='#f8fbff')
        header_frame.pack(fill=tk.X, pady=(20, 15))
        
        tk.Label(
            header_frame,
            text="Информация о студенте",
            font=('Arial', 16, 'bold'),
            bg='#f8fbff', fg='#2c3e50'
        ).pack()
        
        text_frame = tk.Frame(self.root, bg='#f8fbff')
        text_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=10)
        
        text_widget = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=('Arial', 11),
            bg='#e8f4fd',  
            fg='#2c3e50',
            relief='flat',
            padx=15, pady=15,
            height=15
        )
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, student_info)
        text_widget.config(state=tk.DISABLED)
