import os
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO


def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_base64


def generate_html_report(history_df, report_text):
    """Генерирует расширенный HTML-отчёт со всеми графиками"""

    # ============================================================
    # 1. ЛИНЕЙНАЯ ФУНКЦИЯ
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-5, 5, 100)
    y1 = 2 * x + 1
    y2 = x
    y3 = -x + 2
    ax.plot(x, y1, label="y = 2x + 1", color='blue', linewidth=2)
    ax.plot(x, y2, label="y = x", color='green', linewidth=2, linestyle='--')
    ax.plot(x, y3, label="y = -x + 2", color='red', linewidth=2, linestyle='-.')
    ax.scatter([0], [1], color='blue', s=100, label="(0; 1)")
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Линейные функции")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img1 = fig_to_base64(fig)

    # ============================================================
    # 2. КВАДРАТИЧНАЯ ФУНКЦИЯ
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-1, 5, 100)
    y1 = x**2 - 4*x + 3
    y2 = x**2
    y3 = 2*x**2 - 4*x + 1
    ax.plot(x, y1, label="y = x² - 4x + 3", color='green', linewidth=2)
    ax.plot(x, y2, label="y = x²", color='blue', linewidth=2, linestyle='--')
    ax.plot(x, y3, label="y = 2x² - 4x + 1", color='red', linewidth=2, linestyle='-.')
    ax.scatter([2], [-1], color='green', s=100, label="вершина (2; -1)")
    ax.scatter([1, 3], [0, 0], color='orange', s=100, label="корни (1; 0), (3; 0)")
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Квадратичные функции")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img2 = fig_to_base64(fig)

    # ============================================================
    # 3. ПРЕДЕЛ (неопределённость 0/0)
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-1, 5, 200)
    y = (x**2 - 9) / (x - 3)
    ax.plot(x, y, label="(x² - 9)/(x - 3)", color='purple', linewidth=2)
    ax.scatter([3], [6], color='red', s=150, label="предел = 6", zorder=5)
    ax.axhline(y=6, color='red', linestyle='--', alpha=0.5, label="y = 6")
    ax.axvline(x=3, color='gray', linestyle='--', alpha=0.5, label="x = 3")
    ax.set_title("Неопределённость 0/0 и предел")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img3 = fig_to_base64(fig)

    # ============================================================
    # 4. НЕПРЕРЫВНОСТЬ
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-1, 5, 100)
    y = (x - 2)**2 + 1
    ax.plot(x, y, label="y = (x - 2)² + 1", color='teal', linewidth=2)
    ax.scatter([2], [1], color='red', s=150, label="минимум (2; 1)")
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Непрерывная функция")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img4 = fig_to_base64(fig)

    # ============================================================
    # 5. ПРОИЗВОДНАЯ
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-2, 2, 100)
    y = x**3 - 3*x
    y_prime = 3*x**2 - 3
    ax.plot(x, y, label="f(x) = x³ - 3x", color='blue', linewidth=2)
    ax.plot(x, y_prime, label="f'(x) = 3x² - 3", color='red', linestyle='--', linewidth=2)
    ax.scatter([-1, 1], [2, -2], color='green', s=100, label="экстремумы")
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Функция и её производная")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img5 = fig_to_base64(fig)

    # ============================================================
    # 6. ЭЛЕМЕНТАРНЫЕ ФУНКЦИИ
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(-2*np.pi, 2*np.pi, 200)
    ax.plot(x, np.sin(x), label="sin(x)", color='blue', linewidth=2)
    ax.plot(x, np.cos(x), label="cos(x)", color='red', linewidth=2)
    ax.plot(x, np.exp(x/2), label="exp(x/2)", color='green', linewidth=2)
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Элементарные функции")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img6 = fig_to_base64(fig)

    # ============================================================
    # 7. ЛОГАРИФМИЧЕСКАЯ ФУНКЦИЯ
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(0.01, 10, 200)
    ax.plot(x, np.log(x), label="ln(x)", color='purple', linewidth=2)
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)
    ax.set_title("Логарифмическая функция")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img7 = fig_to_base64(fig)

    # ============================================================
    # 8. СХОДИМОСТЬ ГРАДИЕНТНОГО СПУСКА
    # ============================================================
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(history_df["step"], history_df["loss"], marker='o', color='blue', linewidth=2, label="loss")
    ax.axhline(y=2, color='red', linestyle='--', alpha=0.7, label="минимум = 2")
    ax.set_title("Сходимость градиентного спуска")
    ax.set_xlabel("Шаг")
    ax.set_ylabel("Loss")
    ax.grid(True, alpha=0.3)
    ax.legend()
    img8 = fig_to_base64(fig)

    # ============================================================
    # 9. ТАБЛИЦА
    # ============================================================
    table_html = history_df.to_html(classes='styled-table', index=False)

    # ============================================================
    # 10. HTML-СТРАНИЦА
    # ============================================================
    html_content = f"""
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Блок 3. Итоговый мини-проект</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f4f8;
            padding: 30px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #1a2a6c;
            font-size: 32px;
            border-bottom: 4px solid #1a2a6c;
            padding-bottom: 15px;
            margin-bottom: 30px;
            text-align: center;
        }}
        h2 {{
            color: #2c3e50;
            font-size: 24px;
            margin-top: 40px;
            margin-bottom: 15px;
            padding-left: 10px;
            border-left: 6px solid #1a2a6c;
        }}
        .section {{
            background: #f9fafb;
            border-radius: 12px;
            padding: 20px 25px;
            margin-bottom: 30px;
            border: 1px solid #e9ecef;
        }}
        .img-container {{ text-align: center; margin: 20px 0; }}
        .img-container img {{
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        .styled-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
            margin: 20px 0;
        }}
        .styled-table thead tr {{
            background: #1a2a6c;
            color: white;
            text-align: left;
            font-weight: bold;
        }}
        .styled-table th, .styled-table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }}
        .styled-table tbody tr:nth-of-type(even) {{ background: #f3f6fa; }}
        .styled-table tbody tr:hover {{ background: #e2e8f0; }}
        .report-text {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 6px solid #1a2a6c;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            white-space: pre-wrap;
            line-height: 1.6;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #e9ecef;
            color: #7f8c8d;
            font-size: 14px;
        }}
    </style>
</head>
<body>
<div class="container">
    <h1>📊 БЛОК 3. ИТОГОВЫЙ МИНИ-ПРОЕКТ</h1>
    <p style="text-align:center; font-size:18px; color:#555; margin-bottom:30px;">
        Анализ функций, пределов, производных и оптимизация
    </p>

    <div class="section">
        <h2>1. Линейные функции</h2>
        <div class="img-container"><img src="data:image/png;base64,{img1}"></div>
        <p><strong>Сравнение:</strong> y = 2x + 1, y = x, y = -x + 2</p>
    </div>

    <div class="section">
        <h2>2. Квадратичные функции</h2>
        <div class="img-container"><img src="data:image/png;base64,{img2}"></div>
        <p><strong>Сравнение:</strong> y = x² - 4x + 3, y = x², y = 2x² - 4x + 1</p>
    </div>

    <div class="section">
        <h2>3. Предел функции (неопределённость 0/0)</h2>
        <div class="img-container"><img src="data:image/png;base64,{img3}"></div>
        <p><strong>Предел:</strong> lim (x²−9)/(x−3) = 6 при x→3</p>
    </div>

    <div class="section">
        <h2>4. Непрерывная функция</h2>
        <div class="img-container"><img src="data:image/png;base64,{img4}"></div>
        <p><strong>Минимум:</strong> (2; 1), функция непрерывна</p>
    </div>

    <div class="section">
        <h2>5. Производная функции</h2>
        <div class="img-container"><img src="data:image/png;base64,{img5}"></div>
        <p><strong>Производная:</strong> f'(x) = 3x² − 3, экстремумы при x = ±1</p>
    </div>

    <div class="section">
        <h2>6. Элементарные функции</h2>
        <div class="img-container"><img src="data:image/png;base64,{img6}"></div>
        <p><strong>Сравнение:</strong> sin(x), cos(x), exp(x/2)</p>
    </div>

    <div class="section">
        <h2>7. Логарифмическая функция</h2>
        <div class="img-container"><img src="data:image/png;base64,{img7}"></div>
        <p><strong>Функция:</strong> y = ln(x)</p>
    </div>

    <div class="section">
        <h2>8. Градиентный спуск</h2>
        {table_html}
        <p><strong>Результат:</strong> минимум при x ≈ {history_df['x'].iloc[-1]:.4f}, loss ≈ {history_df['loss'].iloc[-1]:.4f}</p>
    </div>

    <div class="section">
        <h2>9. Сходимость градиентного спуска</h2>
        <div class="img-container"><img src="data:image/png;base64,{img8}"></div>
    </div>

    <div class="section">
        <h2>10. Полный аналитический отчёт</h2>
        <div class="report-text">{report_text}</div>
    </div>

    <div class="footer">
        📅 {pd.Timestamp.now().strftime('%d.%m.%Y')} &nbsp;|&nbsp; 👩‍🎓 Яна Чувакова &nbsp;|&nbsp; Блок 3. Основы математики и информатики
    </div>
</div>
</body>
</html>
    """

    with open("data/report.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    full_path = os.path.abspath("data/report.html")
    webbrowser.open(full_path)
    print(f"✅ HTML-ОТЧЁТ ОТКРЫТ В БРАУЗЕРЕ: {full_path}")