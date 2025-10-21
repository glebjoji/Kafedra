#как запустить

1. для установки зависимостей: 
pip install -r "requirements.txt"

2. Проверить конкретный файл:
flake8 src/main.py
pylint src/main.py
black src/main.py
mypy src/main.py
black src/ && flake8 src/ && pylint src/

### Текущие настройки

- Максимальная длина строки: **120 символов**
- Игнорируемые директории: `.git`, `__pycache__`, `.venv`, `venv`, `build`, `dist`
- Некоторые правила отключены для удобства разработки

3. для BD: 
db_name="DB", user="postgres", password="1234", host="localhost", port=5432

4. для создания таблиц: 

-- Создание таблицы teacher
CREATE TABLE teacher (
    teacher_id SERIAL PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    department VARCHAR(100),
    phone VARCHAR(15)
);

-- Создание таблицы elective
CREATE TABLE elective (
    elective_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    hours INTEGER,
    type VARCHAR(20),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

-- Создание таблицы student
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    address TEXT,
    phone VARCHAR(15)
);

-- Создание таблицы enrollment
CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INTEGER,
    elective_id INTEGER,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (elective_id) REFERENCES elective(elective_id)
);

5. запуск: 
python -m src.main

