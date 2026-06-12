import sqlite3

connection = sqlite3.connect("join_lesson06.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

print("База данных подключена")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    position TEXT
)
""")

connection.commit()

print("Таблица employees создана")

cursor.execute("""
CREATE TABLE IF NOT EXISTS work_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    department TEXT,
    position TEXT,
    task_title TEXT,
    hours INTEGER
)
""")

connection.commit()

print("Таблица work_records создана")

cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM work_records")

employees = [
    (1, "Анна", "Бухгалтерия", "главный бухгалтер"),
    (2, "Иван", "Отдел продаж", "менеджер"),
    (3, "Галя", "Отдел продаж", "Руководитель продаж"),
    (4, "Наташа", "Бухгалтерия", "бухгалтер")

]

cursor.executemany(
    "INSERT INTO employees (id, name, department, position) VALUES (?, ?, ?, ?)",
    employees
)

connection.commit()

print("Сотрудники добавлены")

cursor.execute("SELECT * FROM employees")
employees_data = cursor.fetchall()

for employee in employees_data:
    print(employee)

anna_id = employees_data[0][0]
ivan_id = employees_data[1][0]
galya_id = employees_data[2][0]

work_records = [
    (anna_id, "Составить отчёт", 10),
    (anna_id, "Проверить счета", 5),
    (ivan_id, "Позвонить клиентам", 8),
    (galya_id, "Провести планёрку", 2)
]

cursor.executemany(
    "INSERT INTO work_records (employee_id, task_title, hours) VALUES (?, ?, ?)",
    work_records
)

connection.commit()

print("Рабочие записи добавлены")


cursor.execute("SELECT * FROM employees")
employees_rows = cursor.fetchall()

cursor.execute("SELECT * FROM work_records")
work_records_rows = cursor.fetchall()

for row in employees_rows:
    print(row)

for row in work_records_rows:
    print(row)

assert len(employees_rows) >= 3
assert len(work_records_rows) >= 3

cursor.execute("""
SELECT * FROM employees
INNER JOIN work_records ON employees.id = work_records.employee_id
""")
result = cursor.fetchall()

for row in result:
    print(row)

assert len(result) > 0

cursor.execute("""
SELECT * FROM employees
INNER JOIN work_records ON employees.id = work_records.employee_id
WHERE employees.department = 'Отдел продаж'
""")
result = cursor.fetchall()

for row in result:
    print(row)

cursor.execute("""
SELECT * FROM employees
LEFT JOIN work_records ON employees.id = work_records.employee_id
""")
result = cursor.fetchall()

for row in result:
    print(row)

assert len(result) >= len(employees_rows)

cursor.execute("""
SELECT employees.name, COUNT(work_records.id) as task_count
FROM employees
LEFT JOIN work_records ON employees.id = work_records.employee_id
GROUP BY employees.id
""")
result = cursor.fetchall()

print("Отчёт: количество задач по сотрудникам")
for row in result:
    print(f"Сотрудник: {row[0]}, задач: {row[1]}")

assert len(result) > 0

connection.close()



