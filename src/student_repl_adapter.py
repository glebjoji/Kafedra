from src.student_repl_base import Student_repl_base
from src.database_connection import DatabaseConnection
from src.student import Student


class Student_repl_db_adapter(Student_repl_base):


    def __init__(self, db_connection: DatabaseConnection):
        super().__init__(filename=None)
        self.db = db_connection

    def read_all(self):
        with self.db.get_cursor() as cur:
            cur.execute("SELECT * FROM student ORDER BY student_id")
            rows = cur.fetchall()
            return [Student(*row) for row in rows]

    def write_all(self, students):
        with self.db.get_cursor() as cur:
            cur.execute("TRUNCATE TABLE student RESTART IDENTITY CASCADE")
            for s in students:
                cur.execute("""
                    INSERT INTO student (last_name, first_name, middle_name, address, phone)
                    VALUES (%s, %s, %s, %s, %s)
                """, (s.last_name, s.first_name, s.middle_name, s.address, str(s.phone)))

    def add_student(self, student):
        with self.db.get_cursor() as cur:
            cur.execute("""
                INSERT INTO student (last_name, first_name, middle_name, address, phone)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING student_id
            """, (student.last_name, student.first_name, student.middle_name,
                  student.address, str(student.phone)))
            return cur.fetchone()[0]

    def get_count(self):
        with self.db.get_cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM student")
            return cur.fetchone()[0]
