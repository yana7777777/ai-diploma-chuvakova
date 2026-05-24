import sqlite3

print("sqlite3 успешно подключен")

connection = sqlite3.connect("students_lesson01.db")

print("База данных создана или открыта")

cursor = connection.cursor()

print("Cursor создан")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city TEXT,
    age INTEGER,
    course INTEGER,
    faculty TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    gpa REAL DEFAULT 0.0
)
""")

connection.commit()
print("Таблица students создана")

cursor.execute("DELETE FROM students")
connection.commit()


students_data = [
    ("Анна", "Иванова", "Москва", 19, 2, "Информатика", "anna@student.com", "+79111111111", 4.8),
    ("Максим", "Петров", "СПб", 20, 3, "Математика", "maxim@student.com", "+79222222222", 4.5),
    ("Дарья", "Сидорова", "Киев", 18, 1, "Физика", "darya@student.com", "+79333333333", 4.9),
    ("Артем", "Козлов", "Минск", 21, 4, "Информатика", "artem@student.com", "+79444444444", 4.2),
    ("Екатерина", "Морозова", "Москва", 19, 2, "Экономика", "ekaterina@student.com", "+79555555555", 4.7)
]

cursor.executemany("""
INSERT INTO students (first_name, last_name, city, age, course, faculty, email, phone, gpa)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", students_data)


print(f"Добавлено {len(students_data)} студентов")

connection.commit()
print("Изменения сохранены")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\n".join(map(str, students)))

assert len(students) >= 3

for student in students:
    print("ID:", student[0], "| Имя:", student[1], "| Город:", student[2], "| Возраст:", student[3])

cursor.execute(
    "SELECT * FROM students WHERE city = ?",
    ("Москва",)
)

moskva_students = cursor.fetchall()

print("\n".join(map(str, moskva_students)))
print(moskva_students)

assert len(moskva_students) >= 1


connection.close()

print("Соединение с базой данных закрыто")

