import sqlite3

connection = sqlite3.connect("analytics_lesson07.db")
cursor = connection.cursor()

print("База данных подключена")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales_spare_parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    category TEXT,
    article TEXT,
    city TEXT,
    quantity INTEGER,
    price INTEGER,
    revenue INTEGER
)
""")

connection.commit()

print("Таблица sales_spare_parts создана")

cursor.execute("DELETE FROM sales_spare_parts")

sales_spare_parts = [
    ("Шланг подвода химии ф13", "Шланги", "100021", "Самара", 3, 20000, 60000),
    ("Шланг подвода химии ф19", "Шланги", "100022", "Самара", 2, 15000, 30000),
    ("Навивка защитная", "Шланги", "100024", "Самара", 3, 10000, 30000),
    ("Штуцер 1*", "Фитинги", "100044", "Самара", 4, 10000, 40000),
    ("Ниппель ф25 р/в", "Фитинги", "100048", "Самара", 3, 20000, 60000),
    ("Тройник 1*", "Фитинги", "100056", "Самара", 4, 15000, 60000),
    ("Шланг подвода химии ф13", "Шланги", "100021", "Москва", 5, 20000, 100000),
    ("Ниппель ф25 р/в", "Фитинги", "100048", "Москва", 2, 20000, 40000),
    ("Тройник 1*", "Фитинги", "100056", "СПб", 3, 15000, 45000),
    ("Штуцер 1*", "Фитинги", "100044", "Казань", 6, 10000, 60000)
]

cursor.executemany(
    "INSERT INTO sales_spare_parts (product, category, article, city, quantity, price, revenue) VALUES (?, ?, ?, ?, ?, ?, ?)",
    sales_spare_parts
)

connection.commit()
print("Таблица очищена и заполнена 10 уникальными записями")

cursor.execute("SELECT COUNT(*) FROM sales_spare_parts")
count = cursor.fetchone()[0]
print(f"Количество записей: {count}")
assert count >= 10

cursor.execute("SELECT SUM(revenue) FROM sales_spare_parts")
total_revenue = cursor.fetchone()[0]
print(f"Общая выручка: {total_revenue}")
assert total_revenue > 0

cursor.execute("SELECT AVG(price), MIN(price), MAX(price) FROM sales_spare_parts")
avg_price, min_price, max_price = cursor.fetchone()
print(f"Средняя цена: {avg_price}, Мин: {min_price}, Макс: {max_price}")
assert max_price >= min_price

cursor.execute("SELECT category, SUM(revenue) FROM sales_spare_parts GROUP BY category")
result = cursor.fetchall()
for row in result:
    print(f"Категория: {row[0]}, Общая выручка: {row[1]}")
assert len(result) >= 1

cursor.execute("SELECT category, COUNT(*), SUM(revenue), AVG(price) FROM sales_spare_parts GROUP BY category")
result = cursor.fetchall()
for row in result:
    print(f"Категория: {row[0]}, Кол-во: {row[1]}, Общая выручка: {row[2]}, Средняя цена: {row[3]}")

cursor.execute("SELECT category, SUM(revenue) AS total FROM sales_spare_parts GROUP BY category ORDER BY total DESC")
result = cursor.fetchall()
for row in result:
    print(f"Категория: {row[0]}, Общая выручка: {row[1]}")
assert len(result) >= 1

cursor.execute("SELECT category, SUM(revenue) FROM sales_spare_parts GROUP BY category HAVING SUM(revenue) > 100000")
result = cursor.fetchall()
for row in result:
    print(f"Категория: {row[0]}, Общая выручка: {row[1]}")
assert len(result) >= 0
connection.close()