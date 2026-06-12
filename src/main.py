import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from db.connection import get_connection
from db.create_tables import create_main_table
from db.insert_data import insert_all_data
from db.queries import get_all_records, find_by_filter, get_top_records
from db.reports import get_average_value, get_group_report

def print_header(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def print_record(record):
    print(f"ID: {record[0]} | Компания: {record[1]} | Сумма: {record[2]:,.2f} ₽ | Дата: {record[3]} | Категория: {record[4]} | Регион: {record[5]}")

def show_all_records(connection):
    print_header("ВСЕ ЗАПИСИ В ТАБЛИЦЕ REVENUES")
    records = get_all_records(connection)
    if not records:
        print("Нет записей в базе данных.")
    else:
        print(f"Всего записей: {len(records)}\n")
        for record in records:
            print_record(record)
    return records

def search_by_company(connection):
    print_header("ПОИСК ПО КОМПАНИИ")
    company = input("Введите название компании (например, ООО Ромашка): ").strip()
    if not company:
        print("Название компании не может быть пустым.")
        return
    records = find_by_filter(connection, company)
    if not records:
        print(f"Записи для компании '{company}' не найдены.")
    else:
        print(f"\nНайдено записей: {len(records)}\n")
        for record in records:
            print_record(record)
    return records

def show_average_revenue(connection):
    print_header("СРЕДНЯЯ ВЫРУЧКА")
    avg = get_average_value(connection)
    total_records = len(get_all_records(connection))
    print(f"📊 Количество записей в базе: {total_records}")
    print(f"💰 Средняя выручка по всем компаниям: {avg:,.2f} ₽")
    print(f"📈 Максимальная выручка в выборке: {max([r[2] for r in get_all_records(connection)]):,.2f} ₽" if total_records > 0 else "")
    return avg

def show_category_report(connection):
    print_header("ОТЧЁТ ПО КАТЕГОРИЯМ")
    report = get_group_report(connection)
    if not report:
        print("Нет данных для отчёта.")
        return
    print(f"{'Категория':<20} {'Количество записей':<20} {'Доля от общего':<15}")
    print("-" * 55)
    total = sum([row[1] for row in report])
    for row in report:
        percentage = (row[1] / total) * 100 if total > 0 else 0
        print(f"{row[0]:<20} {row[1]:<20} {percentage:.1f}%")
    print("-" * 55)
    print(f"{'ИТОГО:':<20} {total:<20} 100.0%")
    return report

def show_top_records(connection):
    print_header("ТОП ЗАПИСЕЙ ПО ВЫРУЧКЕ")
    try:
        limit = int(input("Введите количество записей для отображения (по умолчанию 3): ") or "3")
        limit = max(1, limit)
    except ValueError:
        limit = 3
        print("Введено некорректное значение. Используем limit = 3.")
    
    records = get_top_records(connection, limit)
    if not records:
        print("Нет данных.")
    else:
        print(f"\n🏆 ТОП-{len(records)} записей по выручке:\n")
        print(f"{'№':<4} {'Компания':<25} {'Выручка (₽)':>15}")
        print("-" * 46)
        for i, row in enumerate(records, 1):
            print(f"{i:<4} {row[0]:<25} {row[1]:>15,.2f}")
    return records

def show_full_analytics(connection):
    print_header("ПОЛНЫЙ АНАЛИТИЧЕСКИЙ ОТЧЁТ")
    print("\n📌 ОБЩАЯ СТАТИСТИКА")
    all_records = get_all_records(connection)
    print(f"   Всего записей: {len(all_records)}")
    
    if all_records:
        total_revenue = sum(r[2] for r in all_records)
        print(f"   Общая выручка: {total_revenue:,.2f} ₽")
        print(f"   Средняя выручка: {get_average_value(connection):,.2f} ₽")
        print(f"   Максимальная выручка: {max(r[2] for r in all_records):,.2f} ₽")
        print(f"   Минимальная выручка: {min(r[2] for r in all_records):,.2f} ₽")
    
    print("\n📌 АНАЛИЗ ПО КОМПАНИЯМ")
    companies = {}
    for r in all_records:
        companies[r[1]] = companies.get(r[1], 0) + r[2]
    for company, total in sorted(companies.items(), key=lambda x: x[1], reverse=True):
        print(f"   {company}: {total:,.2f} ₽")
    
    print("\n📌 АНАЛИЗ ПО КАТЕГОРИЯМ")
    categories = {}
    for r in all_records:
        categories[r[4]] = categories.get(r[4], 0) + 1
    for cat, count in categories.items():
        print(f"   {cat}: {count} записей")
    
    print("\n📌 АНАЛИЗ ПО РЕГИОНАМ")
    regions = {}
    for r in all_records:
        regions[r[5]] = regions.get(r[5], 0) + r[2]
    for region, total in regions.items():
        print(f"   {region}: {total:,.2f} ₽")

def show_menu():
    print("\n" + "=" * 60)
    print(" ГЛАВНОЕ МЕНЮ")
    print("=" * 60)
    print(" 1. Показать все записи")
    print(" 2. Поиск по компании")
    print(" 3. Средняя выручка")
    print(" 4. Отчёт по категориям")
    print(" 5. Топ N записей по выручке")
    print(" 6. Полный аналитический отчёт")
    print(" 7. Выполнить демонстрацию всех функций")
    print(" 0. Выход")
    print("=" * 60)

def main():
    connection = get_connection()
    cursor = connection.cursor()
    
    print("База данных подключена")
    
    # Создание таблицы и заполнение данными при первом запуске
    create_main_table(connection)
    print("Главная таблица revenues создана")
    
    # Проверяем, есть ли данные
    if len(get_all_records(connection)) == 0:
        print("База данных пуста. Добавляем тестовые данные...")
        insert_all_data(connection)
    else:
        print(f"В базе данных уже есть {len(get_all_records(connection))} записей.")
    
    while True:
        show_menu()
        choice = input("\nВыберите действие (0-7): ").strip()
        
        if choice == "0":
            print("\nЗавершение работы...")
            break
        elif choice == "1":
            show_all_records(connection)
        elif choice == "2":
            search_by_company(connection)
        elif choice == "3":
            show_average_revenue(connection)
        elif choice == "4":
            show_category_report(connection)
        elif choice == "5":
            show_top_records(connection)
        elif choice == "6":
            show_full_analytics(connection)
        elif choice == "7":
            show_exam_demo(connection)
        else:
            print("Некорректный ввод. Пожалуйста, выберите 0-7.")
        
        input("\nНажмите Enter, чтобы продолжить...")
    
    connection.close()
    print("\nСоединение закрыто")
    print("ПРОЕКТ ГОТОВ К ЭКЗАМЕНУ!")

def show_exam_demo(connection):
    print_header("ДЕМОНСТРАЦИЯ ВСЕХ ФУНКЦИЙ")
    
    print("\n✅ 1. Все записи:")
    records = get_all_records(connection)
    for record in records:
        print_record(record)
    
    print("\n✅ 2. Поиск по компании 'ООО Ромашка':")
    filtered = find_by_filter(connection, "ООО Ромашка")
    for record in filtered:
        print_record(record)
    
    print("\n✅ 3. Средняя выручка:")
    avg_revenue = get_average_value(connection)
    print(f"   {avg_revenue:,.2f} ₽")
    
    print("\n✅ 4. Отчёт по категориям:")
    report = get_group_report(connection)
    for row in report:
        print(f"   Категория: {row[0]}, Количество: {row[1]}")
    
    print("\n✅ 5. Топ-3 по выручке:")
    top = get_top_records(connection, 3)
    for row in top:
        print(f"   Компания: {row[0]}, Выручка: {row[1]:,.2f} ₽")
    
    print("\n" + "=" * 60)
    print(" ВСЕ ФУНКЦИИ УСПЕШНО ВЫПОЛНЕНЫ")
    print("=" * 60)

if __name__ == "__main__":
    main()
