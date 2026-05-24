import sqlite3

connection = sqlite3.connect("user_lesson02.db")
cursor = connection.cursor()

print("База данных подключена")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    name TEXT,
    surname TEXT,
    city TEXT,
    age INTEGER,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'user',
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP


)
""")

connection.commit()

print("Таблица users создана")

cursor.execute("DELETE FROM users")

users_data = [
    ("alex_smith", "Алексей", "Смит", "Москва", 25, "alex@example.com", "hash_pass_123", "admin", 1),
    ("elena_petrova", "Елена", "Петрова", "Санкт-Петербург", 30, "elena@example.com", "hash_pass_456", "user", 1),
    ("ivan_koval", "Иван", "Коваль", "Киев", 28, "ivan@example.com", "hash_pass_789", "user", 1),
    ("maria_volkova", "Мария", "Волкова", "Минск", 22, "maria@example.com", "hash_pass_abc", "moderator", 1),
    ("dmitry_zhuk", "Дмитрий", "Жук", "Москва", 35, "dmitry@example.com", "hash_pass_def", "user", 0),
    ("olga_sokol", "Ольга", "Сокол", "Санкт-Петербург", 27, "olga@example.com", "hash_pass_ghi", "user", 1),
    ("pavel_moroz", "Павел", "Мороз", "Новосибирск", 29, "pavel@example.com", "hash_pass_jkl", "user", 1),
    ("nata_kuzmin", "Наталья", "Кузьмина", "Екатеринбург", 26, "nata@example.com", "hash_pass_mno", "user", 1)
]

cursor.executemany("""
INSERT INTO users (username, name, surname, city, age, email, password_hash, role, is_active)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", users_data)

connection.commit()
print(f"Таблица users создана и заполнена {len(users_data)} строками")

cursor.execute("SELECT * FROM users")

all_users = cursor.fetchall()

for product in all_users:
    print(product)

assert len(all_users) == 8

cursor.execute("SELECT username, role FROM users")

users_and_role = cursor.fetchall()

for row in users_and_role:
    print(row)

assert len(users_and_role) == 8

cursor.execute(
    "SELECT * FROM users WHERE age > ?",
    (27,)
)

more_users = cursor.fetchall()

for user in more_users:
    print(user)

assert len(more_users) >= 4


cursor.execute(
    "SELECT * FROM users WHERE role = ?",
    ("admin",)
)

role_users = cursor.fetchall()

for user in role_users:
    print(user)

assert len(role_users) == 1

cursor.execute(
    "SELECT * FROM users WHERE city = ? AND age >= ?",
    ("Киев", 28)
)

filtered_and = cursor.fetchall()

print("Пользователь с возростом равным или больше 28")
for user in filtered_and:
    print(user)

cursor.execute(
    "SELECT * FROM users WHERE username = ? OR role = ?",
    ("maria_volkova", "moderator")
)

filtered_or = cursor.fetchall()

print("\nАктивность пользователя:")
for user in filtered_or:
    print(user)

assert len(filtered_and) >= 1
assert len(filtered_or) >= 1

cursor.execute(
    "SELECT * FROM users ORDER BY age DESC LIMIT 3"
)

top_age = cursor.fetchall()

for user in top_age:
    print(user)

assert len(top_age) == 3

connection.close()
print("Соединение закрыто")