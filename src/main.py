import sqlite3

connection = sqlite3.connect("relations_lesson05.db")
cursor = connection.cursor()

print("База данных подключена")

cursor.execute("PRAGMA foreign_keys = ON")

print("Поддержка FOREIGN KEY включена")

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
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    revenue_id INTEGER,
    expense_name TEXT,
    expense_amount REAL,
    category TEXT,
    region TEXT,
    FOREIGN KEY (revenue_id) REFERENCES revenues(id)
)
""")

connection.commit()

print("Таблица expenses создана")

cursor.execute("DELETE FROM revenues")
cursor.execute("DELETE FROM expenses")

connection.commit()

print("Таблицы очищены")

revenues = [
    ("ООО Ромашка", 500000, "2025-05-01", "Продукты", "Москва"),
    ("ООО Ромашка", 300000, "2025-05-10", "Услуги", "СПб"),
    ("ООО Василек", 750000, "2025-05-15", "Продукты", "Казань"),
    ("ООО Василек", 200000, "2025-05-20", "Консультации", "Москва")
]

cursor.executemany(
    "INSERT INTO revenues (company_name, revenue_amount, revenue_date, category, region) VALUES (?, ?, ?, ?, ?)",
    revenues
)

connection.commit()

print("Записи добавлены в таблицу revenues")


cursor.execute("SELECT * FROM revenues")
rows = cursor.fetchall()
for row in rows:
    print(row)

first_id = rows[0][0]
second_id = rows[1][0]

assert first_id is not None
assert second_id is not None

expenses = [
    (1, "Аренда офиса", 100000, "Аренда", "Москва"),
    (1, "Канцтовары", 15000, "Офисные расходы", "Москва"),
    (2, "Реклама", 50000, "Маркетинг", "СПб"),
    (3, "Зарплата", 300000, "Персонал", "Казань"),
    (3, "Коммунальные услуги", 25000, "Коммуналка", "Казань"),
    (4, "Транспорт", 30000, "Логистика", "Москва")
]

cursor.executemany(
    "INSERT INTO expenses (revenue_id, expense_name, expense_amount, category, region) VALUES (?, ?, ?, ?, ?)",
    expenses
)

connection.commit()

print("Записи добавлены в таблицу expenses")

cursor.execute("SELECT * FROM revenues")
revenues_rows = cursor.fetchall()
print("Таблица revenues:")
for row in revenues_rows:
    print(row)

cursor.execute("SELECT * FROM expenses")
expenses_rows = cursor.fetchall()
print("\nТаблица expenses:")
for row in expenses_rows:
    print(row)


assert len(revenues_rows) >= 4
assert len(expenses_rows) >= 4
print("\nПроверка пройдена: в обеих таблицах достаточно записей")

cursor.execute("SELECT * FROM expenses WHERE revenue_id = ?", (1,))
expenses_for_revenue = cursor.fetchall()

print("Расходы для revenue_id = 1:")
for row in expenses_for_revenue:
    print(row)

assert len(expenses_for_revenue) > 0

connection.close()

