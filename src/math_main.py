import pandas as pd
import numpy as np

from src.math.functions import (
    loss_function,
    linear,
    quadratic,
    cubic,
    sin_function,
    cos_function,
    exp_function,
    log_function
)
from src.math.derivatives import (
    loss_derivative,
    linear_derivative,
    quadratic_derivative,
    cubic_derivative,
    sin_derivative,
    cos_derivative,
    exp_derivative,
    log_derivative
)
from src.math.optimization import gradient_descent
from src.math.report_utils import save_report
from src.math.report_html import generate_html_report
from src.math.chat_bot import open_chat_bot
from src.math.smart_chat_bot import open_smart_chat


def main():
    print("=" * 100)
    print("БЛОК 3: ИТОГОВЫЙ МИНИ-ПРОЕКТ")
    print("ПОЛНЫЙ АНАЛИЗ ФУНКЦИЙ, ПРЕДЕЛОВ, ПРОИЗВОДНЫХ И ОПТИМИЗАЦИИ")
    print("=" * 100)

    # ================================================================
    # 1. ЛИНЕЙНАЯ ФУНКЦИЯ
    # ================================================================
    print("\n" + "=" * 100)
    print("1. ЛИНЕЙНАЯ ФУНКЦИЯ y = 2x + 1")
    print("=" * 100)

    x_vals = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    y_vals = linear(x_vals)

    print("\nТаблица значений:")
    table_linear = pd.DataFrame({"x": x_vals, "y = 2x + 1": y_vals})
    print(table_linear.to_string(index=False))

    print("\nАнализ:")
    print(f"  - Коэффициент k = 2 (угол наклона)")
    print(f"  - Коэффициент b = 1 (смещение по оси y)")
    print(f"  - Пересечение с осью y: (0; {linear(0)})")
    print(f"  - Пересечение с осью x: x = {-1/2:.1f}")
    print(f"  - Функция монотонно возрастает (k > 0)")
    print(f"  - Производная: f'(x) = {linear_derivative(0)} (константа)")

    # ================================================================
    # 2. КВАДРАТИЧНАЯ ФУНКЦИЯ
    # ================================================================
    print("\n" + "=" * 100)
    print("2. КВАДРАТИЧНАЯ ФУНКЦИЯ y = x² - 4x + 3")
    print("=" * 100)

    x_quad_vals = np.array([-1, 0, 1, 2, 3, 4, 5])
    y_quad_vals = quadratic(x_quad_vals)

    print("\nТаблица значений:")
    table_quad = pd.DataFrame({"x": x_quad_vals, "y = x² - 4x + 3": y_quad_vals})
    print(table_quad.to_string(index=False))

    a, b, c = 1, -4, 3
    vertex_x = -b / (2 * a)
    vertex_y = quadratic(vertex_x)
    discriminant = b**2 - 4*a*c
    roots = []
    if discriminant > 0:
        root1 = (-b - np.sqrt(discriminant)) / (2*a)
        root2 = (-b + np.sqrt(discriminant)) / (2*a)
        roots = [root1, root2]

    print("\nАнализ:")
    print(f"  - Коэффициенты: a = {a}, b = {b}, c = {c}")
    print(f"  - Вершина: ({vertex_x:.1f}; {vertex_y:.1f})")
    print(f"  - Дискриминант: D = {discriminant}")
    if discriminant > 0:
        print(f"  - Корни: x₁ = {roots[0]:.1f}, x₂ = {roots[1]:.1f}")
    elif discriminant == 0:
        print(f"  - Корень: x = {roots[0]:.1f} (двойной)")
    else:
        print("  - Корней нет (D < 0)")
    print(f"  - Ветви направлены вверх (a > 0)")
    print(f"  - Минимальное значение: {vertex_y:.1f} в точке x = {vertex_x:.1f}")
    print(f"  - Производная: f'(x) = 2x - 4")
    print(f"  - Производная в вершине: {quadratic_derivative(vertex_x)}")

    # ================================================================
    # 3. ПРЕДЕЛ ФУНКЦИИ (неопределённость 0/0)
    # ================================================================
    print("\n" + "=" * 100)
    print("3. ПРЕДЕЛ ФУНКЦИИ (неопределённость 0/0)")
    print("=" * 100)

    print("\nФункция: f(x) = (x² - 9)/(x - 3)")
    print("Анализ:")
    print("  - При x = 3: числитель = 0, знаменатель = 0 → неопределённость 0/0")
    print("  - Разложение числителя: x² - 9 = (x - 3)(x + 3)")
    print("  - После сокращения: f(x) = x + 3 (при x ≠ 3)")
    print("  - Предел при x → 3: lim f(x) = 3 + 3 = 6")

    x_near = [2.9, 2.99, 2.999, 3.001, 3.01, 3.1]
    y_near = [(x**2 - 9)/(x - 3) for x in x_near]
    df_near = pd.DataFrame({"x": x_near, "f(x)": y_near})
    print("\nПриближение к пределу:")
    print(df_near.to_string(index=False))
    print("  - Видно, что при x → 3 значение стремится к 6")

    # ================================================================
    # 4. НЕПРЕРЫВНОСТЬ ФУНКЦИИ
    # ================================================================
    print("\n" + "=" * 100)
    print("4. НЕПРЕРЫВНАЯ ФУНКЦИЯ y = (x - 2)² + 1")
    print("=" * 100)

    x_cont_vals = np.array([-1, 0, 1, 2, 3, 4, 5])
    y_cont_vals = (x_cont_vals - 2)**2 + 1

    print("\nТаблица значений:")
    table_cont = pd.DataFrame({"x": x_cont_vals, "y = (x - 2)² + 1": y_cont_vals})
    print(table_cont.to_string(index=False))

    print("\nАнализ:")
    print("  - Функция определена при всех x ∈ ℝ")
    print("  - Минимальное значение: 1 в точке x = 2")
    print("  - Функция непрерывна на всей области определения")
    print("  - Нет точек разрыва")
    print("  - Область значений: [1; +∞)")

    # ================================================================
    # 5. ПРОИЗВОДНАЯ ФУНКЦИИ
    # ================================================================
    print("\n" + "=" * 100)
    print("5. ПРОИЗВОДНАЯ ФУНКЦИИ y = x³ - 3x")
    print("=" * 100)

    x_der_vals = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    y_der_vals = cubic(x_der_vals)
    y_der_prime_vals = cubic_derivative(x_der_vals)

    print("\nТаблица значений:")
    table_der = pd.DataFrame({
        "x": x_der_vals,
        "f(x) = x³ - 3x": y_der_vals,
        "f'(x) = 3x² - 3": y_der_prime_vals
    })
    print(table_der.to_string(index=False))

    print("\nАнализ:")
    print("  - Функция: f(x) = x³ - 3x")
    print("  - Производная: f'(x) = 3x² - 3")
    print("  - Точки экстремума (f'(x) = 0): x = -1, x = 1")
    print(f"  - f(-1) = {cubic(-1)} → локальный максимум")
    print(f"  - f(1) = {cubic(1)} → локальный минимум")

    # ================================================================
    # 6. ЭЛЕМЕНТАРНЫЕ ФУНКЦИИ
    # ================================================================
    print("\n" + "=" * 100)
    print("6. ЭЛЕМЕНТАРНЫЕ ФУНКЦИИ (справочные значения)")
    print("=" * 100)

    x_elem = np.array([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    print("\nТаблица значений элементарных функций при x = [-π, -π/2, 0, π/2, π]:")
    table_elem = pd.DataFrame({
        "x": x_elem,
        "sin(x)": sin_function(x_elem),
        "cos(x)": cos_function(x_elem),
        "exp(x)": exp_function(x_elem),
        "ln(x+1)": log_function(x_elem)
    })
    print(table_elem.to_string(index=False))

    # ================================================================
    # 7. ГРАДИЕНТНЫЙ СПУСК
    # ================================================================
    print("\n" + "=" * 100)
    print("7. ГРАДИЕНТНЫЙ СПУСК")
    print("=" * 100)

    history = gradient_descent(
        start_x=-2,
        learning_rate=0.2,
        steps=20
    )

    history_df = pd.DataFrame(history)

    print("\nТаблица шагов градиентного спуска:")
    print(history_df.to_string(index=False))

    final_x = history_df["x"].iloc[-1]
    final_loss = history_df["loss"].iloc[-1]
    start_x = history_df["x"].iloc[0]
    start_loss = history_df["loss"].iloc[0]

    print("\nАнализ градиентного спуска:")
    print(f"  - Начальное значение x: {start_x}")
    print(f"  - Начальное значение loss: {start_loss:.4f}")
    print(f"  - Финальное значение x: {final_x:.6f}")
    print(f"  - Финальное значение loss: {final_loss:.6f}")
    print(f"  - Изменение x: {final_x - start_x:.4f}")
    print(f"  - Улучшение loss: {start_loss - final_loss:.4f}")
    print(f"  - Количество шагов: 20")
    print(f"  - Скорость обучения: 0.2")
    print(f"  - Точность: достигнут минимум с погрешностью ~{final_loss - 2:.6f}")

    # ================================================================
    # 8. ОТЧЁТ
    # ================================================================
    report = f"""
{"=" * 100}
БЛОК 3: ИТОГОВЫЙ МИНИ-ПРОЕКТ
ПОЛНЫЙ АНАЛИЗ ФУНКЦИЙ, ПРЕДЕЛОВ, ПРОИЗВОДНЫХ И ОПТИМИЗАЦИИ
{"=" * 100}

1. ЛИНЕЙНАЯ ФУНКЦИЯ
   {"-" * 60}
   Функция: y = 2x + 1
   Коэффициенты: k = 2, b = 1
   Пересечение с y: (0; 1)
   Пересечение с x: (-0.5; 0)
   Производная: f'(x) = 2
   Свойства: монотонно возрастает

2. КВАДРАТИЧНАЯ ФУНКЦИЯ
   {"-" * 60}
   Функция: y = x² - 4x + 3
   Коэффициенты: a = 1, b = -4, c = 3
   Вершина: (2; -1)
   Дискриминант: D = 4
   Корни: x₁ = 1, x₂ = 3
   Ветви направлены вверх
   Минимальное значение: -1
   Производная: f'(x) = 2x - 4

3. ПРЕДЕЛ ФУНКЦИИ
   {"-" * 60}
   Функция: f(x) = (x² - 9)/(x - 3)
   Неопределённость 0/0 при x = 3
   После сокращения: f(x) = x + 3
   Предел при x → 3: 6

4. НЕПРЕРЫВНОСТЬ
   {"-" * 60}
   Функция: y = (x - 2)² + 1
   Минимум: (2; 1)
   Область определения: ℝ
   Область значений: [1; +∞)
   Функция непрерывна на всей области определения

5. ПРОИЗВОДНАЯ
   {"-" * 60}
   Функция: f(x) = x³ - 3x
   Производная: f'(x) = 3x² - 3
   Точки экстремума: x = -1 (максимум), x = 1 (минимум)
   f(-1) = 2, f(1) = -2

6. ЭЛЕМЕНТАРНЫЕ ФУНКЦИИ
   {"-" * 60}
   sin(x): периодическая, нечётная
   cos(x): периодическая, чётная
   exp(x): монотонно возрастает
   ln(x+1): определена при x > -1

7. ГРАДИЕНТНЫЙ СПУСК
   {"-" * 60}
   Начальное значение x: {start_x}
   Начальное значение loss: {start_loss:.4f}
   Финальное значение x: {final_x:.6f}
   Финальное значение loss: {final_loss:.6f}
   Изменение x: {final_x - start_x:.4f}
   Улучшение loss: {start_loss - final_loss:.4f}
   Количество шагов: 20
   Скорость обучения: 0.2
   Минимум функции: x = 3, loss = 2

8. ВЫВОДЫ
   {"-" * 60}
   - Градиентный спуск успешно нашёл минимум функции loss(x) = (x - 3)² + 2
   - Все изученные темы блока 3 применены в одном проекте
   - Проект демонстрирует базовые навыки Python для анализа данных
   - Код разбит на модули: functions, derivatives, optimization, report_utils, report_html

9. РЕКОМЕНДАЦИИ
   {"-" * 60}
   - Для ускорения сходимости можно увеличить learning_rate до 0.5
   - Для повышения точности увеличить количество шагов до 50-100
   - Использовать адаптивные методы оптимизации (Adam, RMSprop)
   - Добавить нормализацию данных для реальных задач
   - Использовать разбиение на обучающую и тестовую выборки

{"=" * 100}
ДАТА: {pd.Timestamp.now().strftime('%d.%m.%Y')}
СТУДЕНТ: Яна Чувакова
{"=" * 100}
"""

    save_report(report, "data/project_report.txt")
    print("\n✅ ТЕКСТОВЫЙ ОТЧЁТ СОХРАНЁН в data/project_report.txt")

    # ================================================================
    # 9. HTML-ОТЧЁТ
    # ================================================================
    print("\n" + "=" * 100)
    print("8. СОЗДАНИЕ HTML-ОТЧЁТА С ВИЗУАЛИЗАЦИЕЙ")
    print("=" * 100)

    generate_html_report(history_df, report)

    # Открываем простой бот
    open_chat_bot()

    # Открываем умный бот
    open_smart_chat()

    print("\n" + "=" * 100)
    print("✅ ПРОЕКТ УСПЕШНО ЗАВЕРШЁН!")
    print("=" * 100)


# ================================================================
# ТОЛЬКО ЭТОТ БЛОК ДОЛЖЕН БЫТЬ В КОНЦЕ ФАЙЛА!
# ================================================================
if __name__ == "__main__":
    main()
    



