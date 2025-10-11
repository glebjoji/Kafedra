from src.database_connection import DatabaseConnection
from src.student_repl_adapter import Student_repl_db_adapter

def main():
    db = DatabaseConnection(
        db_name="DB",
        user="postgres",
        password="1234",
        host="localhost",
        port=5432
    )

    repo = Student_repl_db_adapter(db)

    print(f"Всего студентов: {repo.get_count()}")

    first = repo.get_by_id(1)
    if first:
        print("Первый студент:")
        print(first)
    else:
        print("Студент с ID=1 не найден.")

if __name__ == "__main__":
    main()
