from src.core.student import Student

class StudentSummary(Student):
    def __init__(self, student: Student):
        super().__init__(
            student.student_id,
            student.last_name,
            student.first_name,
            student.middle_name,
            student.address,
            student.phone
        )


    def __str__(self):
        return f"{self.last_name} {self.phone}"