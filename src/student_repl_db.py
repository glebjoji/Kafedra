import psycopg2
from src.student import Student
from src.student_repl_base import Student_repl_base


class Student_repl_db(Student_repl_base):
    def __init__(self, db_name, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.conn.autocommit = True

    #реализация абстрактных методов из базового класса
    def read_all(self):
        #Считать все записи из таблицы student
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM student ORDER BY student_id")
            rows = cur.fetchall()
            return [Student(*row) for row in rows]

    def write_all(self, students):
        #Полная перезапись таблицы student
        with self.conn.cursor() as cur:
            cur.execute("TRUNCATE TABLE student RESTART IDENTITY CASCADE")
            for s in students:
                cur.execute("""
                    INSERT INTO student (last_name, first_name, middle_name, address, phone)
                    VALUES (%s, %s, %s, %s, %s)
                """, (s.last_name, s.first_name, s.middle_name, s.address, str(s.phone)))

    def get_by_id(self, student_id):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM student WHERE student_id = %s", (student_id,))
            row = cur.fetchone()
            return Student(*row) if row else None

    def get_k_n_short_list(self, k, n):
        offset = (n - 1) * k
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM student ORDER BY student_id LIMIT %s OFFSET %s", (k, offset))
            rows = cur.fetchall()
            return [Student(*row) for row in rows]


    def add_student(self, student):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO student (last_name, first_name, middle_name, address, phone)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING student_id
            """, (student.last_name, student.first_name, student.middle_name,
                  student.address, str(student.phone)))
            return cur.fetchone()[0]


    def update_student(self, student_id, new_student):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE student
                SET last_name = %s,
                    first_name = %s,
                    middle_name = %s,
                    address = %s,
                    phone = %s
                WHERE student_id = %s
            """, (new_student.last_name, new_student.first_name, new_student.middle_name,
                  new_student.address, str(new_student.phone), student_id))
            return cur.rowcount > 0


    def delete_student(self, student_id):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM student WHERE student_id = %s", (student_id,))
            return cur.rowcount > 0


    def get_count(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM student")
            return cur.fetchone()[0]

    def __del__(self):
        if hasattr(self, "conn") and self.conn:
            self.conn.close()
