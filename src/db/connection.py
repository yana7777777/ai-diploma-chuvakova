# import sqlite3

# print("sqlite3 успешно подключен")

# connection = sqlite3.connect("students_lesson01.db")

# print("База данных создана или открыта")

# cursor = connection.cursor()

# print("Cursor создан")


# connection.commit()
# print("Таблица students создана")

# connection.commit()
# print("Изменения сохранены")

# cursor.execute("SELECT * FROM students")

# students = cursor.fetchall()

# print("\n".join(map(str, students)))

# assert len(students) >= 3



# connection.close()

# print("Соединение с базой данных закрыто")

