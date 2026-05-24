import sqlite3

connection = sqlite3.connect("user_lesson03.db")
cursor = connection.cursor()

print("База подключена")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT,
    salary INTEGER,
    hire_date DATE,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    city TEXT,
    experience_years INTEGER DEFAULT 0,
    status TEXT DEFAULT 'active',
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
print("Таблица employees создана (13 полей)")

cursor.execute("DELETE FROM employees")

connection.commit()

print("Таблица очищена")

employees = [
    ("Иван", "Петров", "Разработчик", "IT", 120000, "2020-01-15", "ivan@company.com", "+79123456789", "Москва", 5, "active", 1),
    ("Елена", "Сидорова", "Менеджер", "Продажи", 95000, "2019-03-10", "elena@company.com", "+79234567890", "СПб", 7, "active", 1),
    ("Алексей", "Козлов", "Тестировщик", "QA", 80000, "2021-06-20", "alexey@company.com", "+79345678901", "Новосибирск", 3, "active", 1)
]

cursor.executemany("""
    INSERT INTO employees (first_name, last_name, position, department, salary, hire_date, email, phone, city, experience_years, status, is_active)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", employees)

connection.commit()
print(f"Добавлено {len(employees)} сотрудников")

cursor.execute("SELECT * FROM employees")

employees_data = cursor.fetchall()

for employee in employees_data:
    print(employee)

assert len(employees_data) == 3

cursor.execute(
    "UPDATE employees SET position = ? WHERE first_name = ?",
    ("Коммерческий директор", "Елена")
)

connection.commit()

print("Должность обновлена")

cursor.execute(
    "SELECT * FROM employees WHERE first_name = ?",
    ("Елена",)
)

elena = cursor.fetchone()
print(elena)

# Проверяем, что должность соответствует ожидаемой
assert elena[3] == "Коммерческий директор"  # position на индексе 3 (или проверьте индекс)
print("Assert пройден!")


cursor.execute(
    "DELETE FROM employees WHERE first_name = ?",
    ("Елена",)
)

connection.commit()

print("Запись удалена")

cursor.execute("SELECT * FROM employees")

employees_after_delete = cursor.fetchall()

for employee in employees_after_delete:
    print(employee)

assert len(employees_after_delete) == 2

connection.close()

print("Соединение закрыто")