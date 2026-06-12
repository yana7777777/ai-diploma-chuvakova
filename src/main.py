import sqlite3

print("sqlite3 подключен")

def get_connection(db_name="python_sql_lesson08.db"):
    connection = sqlite3.connect(db_name)
    return connection

connection = get_connection()

print("Подключение создано")

assert connection is not None


def create_employees_table(connection):
  cursor = connection.cursor()
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS employees (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      department TEXT,
      position TEXT
  )
  """)

  connection.commit()

create_employees_table(connection)

print("Таблица employees создана")


def clear_employees(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees")
    # Если PRIMARY KEY был задан с AUTOINCREMENT, необходимо сбросить
    # счетчик в таблице sqlite_sequence, чтобы ID начинались с 1.
    # Без этого новые записи будут продолжать нумерацию с последнего
    # максимального ID, который когда-либо был в таблице.
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='employees'")
    connection.commit()

clear_employees(connection)

print("Таблица employees очищена и счетчик ID сброшен")


def add_employees (connection, name, department, position):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO employees  (name, department, position) VALUES (?, ?, ?)",
        (name, department, position)
    )
    connection.commit()

add_employees (connection, "Анна", "Бухгалтерия", "Главный бухгалтер")
add_employees (connection, "Иван", "Отдел продаж", "Менеджер")
add_employees (connection, "Наташа", "Бухгалтерия", "Бухгалтер")

print("Сотрудники добавлены")



def get_all_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()

employees = get_all_employees(connection)

for employee in employees:
    print(employee)

assert len(employees) == 3


def find_employees_by_position(connection, position):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM employees WHERE position = ?",
        (position,)
    )
    return cursor.fetchall()

account_employees = find_employees_by_position(connection, "Менеджер")

for employee in account_employees:
    print(employee)

assert len(account_employees) == 1


def find_employees_by_name(connection, name):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM employees WHERE name = ?",
        (name,)
    )
    return cursor.fetchall()

account_employees = find_employees_by_name(connection, "Иван")

for employee in account_employees:
    print(employee)

assert len(account_employees) == 1


def update_employees_position(connection, name, new_position):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE employees SET position = ? WHERE name = ?",
        (new_position, name)
    )
    connection.commit()

update_employees_position(connection, "Иван", "Руководитель")

ivan_updated = find_employees_by_name(connection, "Иван")

print(ivan_updated)

assert ivan_updated[0][3] == "Руководитель"


def delete_employees(connection, name):
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM employees WHERE name = ?",
        (name,)
    )
    connection.commit()

delete_employees(connection, "Иван")

employees_after_delete = get_all_employees(connection)

for employee in employees_after_delete:
    print(employee)

assert len(employees_after_delete) == 2

connection.close()

print("Соединение закрыто")