import sqlite3

connection = sqlite3.connect("design_lesson04.db")
cursor = connection.cursor()

print("База данных подключена")

project_topic = "My topic is Finance"  
print(project_topic)

cursor.execute("""
CREATE TABLE IF NOT EXISTS revenues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    revenue_amount REAL,
    revenue_date TEXT,
    category TEXT,
    region TEXT
)
""")

connection.commit()

print("Таблица revenues создана")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee_salaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    department TEXT,
    position TEXT,
    salary REAL,
    payment_date TEXT
)
""")

connection.commit()

print("Таблица employee_salaries создана")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_category TEXT,
    expense_name TEXT,
    amount REAL,
    expense_date TEXT,
    responsible_person TEXT
)
""")

connection.commit()

print("Таблица expenses создана")

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table'
""")

tables = cursor.fetchall()

print("Таблицы в базе:")
for table in tables:
    print(table)

assert len(tables) >= 3

cursor.execute("""
INSERT INTO revenues (company_name, revenue_amount, revenue_date, category, region) VALUES
('ООО Ромашка', 500000, '2025-05-01', 'Продукты', 'Москва'),
('ООО Ромашка', 300000, '2025-05-10', 'Услуги', 'СПб'),
('ООО Василек', 750000, '2025-05-15', 'Продукты', 'Казань'),
('ООО Василек', 200000, '2025-05-20', 'Консультации', 'Москва')
""")

connection.commit()

print("записи добавлены в таблицу revenues")

cursor.execute("""
INSERT INTO employee_salaries (employee_name, department, position, salary, payment_date) VALUES
('Иванов Иван', 'Sales', 'Менеджер', 80000, '2025-05-25'),
('Петрова Анна', 'Sales', 'Старший менеджер', 120000, '2025-05-25'),
('Сидоров Петр', 'IT', 'Программист', 150000, '2025-05-25'),
('Козлова Мария', 'Marketing', 'Маркетолог', 90000, '2025-05-25')
""")

connection.commit()
print("записи добавлены в employee_salaries")

cursor.execute("""
INSERT INTO expenses (expense_category, expense_name, amount, expense_date, responsible_person) VALUES
('Офис', 'Аренда офиса', 100000, '2025-05-01', 'Иванов Иван'),
('Офис', 'Канцтовары', 15000, '2025-05-05', 'Петрова Анна'),
('Зарплата', 'Выдача зарплаты', 500000, '2025-05-25', 'Сидоров Петр'),
('Реклама', 'Реклама в интернете', 50000, '2025-05-15', 'Козлова Мария')
""")

connection.commit()
print("Записи добавлены в таблицу expenses")



cursor.execute("SELECT * FROM revenues")
rows = cursor.fetchall()
for row in rows:
    print(row)
assert len(rows) >= 2


cursor.execute("SELECT * FROM employee_salaries")
rows = cursor.fetchall()
for row in rows:
    print(row)
assert len(rows) >= 2



for table_name in ["revenues", "employee_salaries", "expenses"]:
    print("\nТаблица:", table_name)
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    assert len(rows) >= 1

connection.close()

print("Соединение закрыто")