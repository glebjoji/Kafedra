"""
Модуль с главным окном приложения (View слоя MVC).
Добавлена кнопка "Удалить" с подтверждением удаления.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from typing import List


class MainWindow:
    
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Студенты")
        self.root.geometry("950x650")
        self.root.minsize(600, 300)
        self.root.configure(bg='#f8fbff')
        self.setup_styles()
        self.setup_ui()
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Header.TLabel', background='#f8fbff', font=('Arial', 18, 'bold'))
        style.configure('Students.Treeview', background='#e8f4fd', font=('Arial', 11))
        style.configure('Students.Treeview.Heading', background='#3498db', foreground='white', font=('Arial', 12, 'bold'))
        style.configure('Vertical.TScrollbar', background="#0d00ff", troughcolor='#d6eaf8', borderwidth=0)
    
    def setup_ui(self):
        header_frame = tk.Frame(self.root, bg='#f8fbff')
        header_frame.pack(fill=tk.X, pady=(20, 15))
        
        header_label = tk.Label(
            header_frame, 
            text="📚 Студенты", 
            font=('Arial', 22, 'bold'),
            bg='#f8fbff', fg='#2c3e50'
        )
        header_label.pack()

        table_frame = tk.Frame(self.root, bg='#f8fbff')
        table_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=10)
        
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, style='Vertical.TScrollbar')
        
        self.tree = ttk.Treeview(
            table_frame, 
            columns=("info",), 
            show="headings",
            height=22,
            style='Students.Treeview',
            yscrollcommand=v_scrollbar.set
        )
        
        self.tree.heading("info", text="Фамилия И.О. (телефон)")
        self.tree.column("info", width=850, anchor=tk.W)
        
        v_scrollbar.config(command=self.tree.yview)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Кнопки управления
        btn_frame = tk.Frame(self.root, bg='#f8fbff')
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Добавить",
            font=('Arial', 12, 'bold'),
            bg='#27ae60', fg='white',
            relief='flat', width=12, height=1,
            cursor='hand2',
            command=lambda: self.controller.on_add_student_requested()
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Редактировать",
            font=('Arial', 12, 'bold'),
            bg='#f39c12', fg='white',
            relief='flat', width=12, height=1,
            cursor='hand2',
            command=lambda: self.controller.on_edit_student_requested()
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Удалить", 
            font=('Arial', 12, 'bold'),
            bg='#e74c3c', fg='white',
            relief='flat', width=12, height=1,
            cursor='hand2',
            command=lambda: self.controller.on_delete_student_requested()
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Подробности",
            font=('Arial', 12, 'bold'),
            bg='#3498db', fg='white',
            relief='flat', width=12, height=1,
            cursor='hand2',
            command=lambda: self.controller.on_details_requested()
        ).pack(side=tk.LEFT, padx=5)

    def refresh_table(self, data: List[str]):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in data:
            self.tree.insert("", tk.END, values=(row,))
    
    def get_selected_item(self) -> str | None:
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            return item['values'][0]
        return None
    
    def show_warning(self, message: str):
        messagebox.showwarning("Предупреждение", message, parent=self.root)
    
    def show_error(self, message: str):
        messagebox.showerror("Ошибка", message, parent=self.root)
    
    def show_success(self, message: str):
        messagebox.showinfo("Успех", message, parent=self.root)
    
    def show_delete_confirmation(self, message: str) -> bool:
        result = messagebox.askyesno(
            title="Подтверждение удаления",
            message=message,
            icon='warning',
            parent=self.root
        )
        return result
    
    def run(self):
        self.root.mainloop()