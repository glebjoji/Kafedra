from src.student import Student


class StudentSummary:

    def __init__(self, student: Student):
        self._student = student  

    @property
    def last_name(self):
        return self._student.last_name

    @property
    def phone(self):
        return self._student.phone

    def __str__(self):
        return f"{self.last_name} {self.phone}"