import sqlite3

print("sqlite3 успешно подключен")

connection = sqlite3.connect("students_lesson01.db")

print("База данных создана или открыта")

cursor = connection.cursor()

print("Cursor создан")

