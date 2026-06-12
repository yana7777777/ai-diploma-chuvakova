import sqlite3

def get_connection(db_name="lesson09_employees.db"):
    connection = sqlite3.connect(db_name)
    return connection

connection = get_connection()
cursor = connection.cursor()

print("База данных подключена")
assert connection is not None


def create_employees_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        department TEXT,
        position TEXT,
        hire_date TEXT,
        salary INTEGER,
        is_active INTEGER,
        rating REAL
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

def add_employee(connection, full_name, department, position, hire_date, salary, is_active, rating):
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO employees (full_name, department, position, hire_date, salary, is_active, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (full_name, department, position, hire_date, salary, is_active, rating)
    )
    connection.commit()

# Добавляем сотрудников (как в candidates - 7 полей)
add_employee(connection, "Анна Смирнова", "Бухгалтерия", "Главный бухгалтер", "2020-03-15", 85000, 1, 4.8)
add_employee(connection, "Иван Петров", "Отдел продаж", "Менеджер", "2021-06-10", 65000, 1, 4.2)
add_employee(connection, "Ольга Иванова", "IT отдел", "Python Developer", "2022-01-20", 120000, 1, 4.9)
add_employee(connection, "Павел Соколов", "Отдел продаж", "Старший менеджер", "2019-11-01", 85000, 1, 4.5)
add_employee(connection, "Мария Кузнецова", "Бухгалтерия", "Бухгалтер", "2023-02-14", 55000, 0, 3.9)

print("Сотрудники добавлены")


def get_all_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()

employees = get_all_employees(connection)

for employee in employees:
    print(employee)

assert len(employees) == 5

def find_employees_by_is_active(connection, is_active):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM employees WHERE is_active = ?",
        (is_active,)
    )
    return cursor.fetchall()

is_active_employee = find_employees_by_is_active(connection, 0)

print("Новые кандидаты:")
for employee in is_active_employee:
    print(employee)

assert len(is_active_employee) == 1


def update_record(connection, employee_id, new_position, new_salary):
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE employees SET position = ?, salary = ? WHERE id = ?",
        (new_position, new_salary, employee_id)
    )
    connection.commit()

update_record(connection, 1, "Финансовый директор", 120000)

cursor.execute("SELECT * FROM employees WHERE id = 1")
updated_employee = cursor.fetchone()
print(updated_employee)

assert updated_employee[3] == "Финансовый директор"
assert updated_employee[5] == 120000


def get_group_report(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT department, COUNT(*), AVG(salary) FROM employees GROUP BY department")
    return cursor.fetchall()

report = get_group_report(connection)

for row in report:
    print(f"Отдел: {row[0]}, Сотрудников: {row[1]}, Средняя зарплата: {row[2]}")

assert len(report) >= 1


def get_top_records(connection, limit=3):
    cursor = connection.cursor()
    cursor.execute("SELECT full_name, salary FROM employees ORDER BY salary DESC LIMIT ?", (limit,))
    return cursor.fetchall()

top_records = get_top_records(connection, 3)

for row in top_records:
    print(f"Сотрудник: {row[0]}, Зарплата: {row[1]}")

assert len(top_records) == 3


def show_project_summary(connection):
    print("\n--- ОТЧЁТ ПО СОТРУДНИКАМ ---")
    
    employees = get_all_employees(connection)
    print(f"Всего сотрудников: {len(employees)}")
    
    active = find_employees_by_is_active(connection, 1)
    print(f"Активных сотрудников: {len(active)}")
    
    report = get_group_report(connection)
    print("\nОтделы:")
    for row in report:
        print(f"  {row[0]}: {row[1]} чел., средняя з/п {row[2]:.0f}")
    
    top = get_top_records(connection, 3)
    print("\nТоп-3 по зарплате:")
    for row in top:
        print(f"  {row[0]}: {row[1]}")

show_project_summary(connection)
connection.close()
print("Соединение закрыто")

