"""
Модуль с реализацией паттерна Наблюдатель для репозитория студентов.
"""

from typing import Callable, List
from src.data.student_repl_base import Student_repl_base

class RepositoryObserver:
    
    def __init__(self, repo: Student_repl_base):
        self.repo = repo
        self._subscribers: List[Callable] = []
    
    def subscribe(self, callback: Callable):
        self._subscribers.append(callback)
    
    def unsubscribe(self, callback: Callable):
        if callback in self._subscribers:
            self._subscribers.remove(callback)
    
    def notify_data_loaded(self, short_list: List[str]):
        for callback in self._subscribers:
            callback(short_list)
    
    def fetch_short_list(self, k: int, n: int) -> List[str]:
        return self.repo.get_k_n_short_list(k, n)
    
    def fetch_student_by_short_info(self, short_info: str):
        all_students = self.repo.read_all()
        for student in all_students:
            if student.short_info() == short_info:
                return student
        return None
