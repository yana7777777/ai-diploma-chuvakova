
from flask import Flask, request
from src.db.connection import get_connection
from src.db.queries import get_all_records, find_by_filter, get_top_records
from src.db.reports import get_average_value, get_group_report
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Анализ доходов компании</title>
    <style>
        body { font-family: Arial; margin: 20px; background: #f0f0f0; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { color: #2c3e50; text-align: center; }
        .menu { background: #2c3e50; padding: 15px; border-radius: 10px; margin: 20px 0; }
        .menu a { color: white; text-decoration: none; margin-right: 20px; padding: 8px 15px; border-radius: 5px; }
        .menu a:hover { background: #3498db; }
        table { border-collapse: collapse; width: 100%; background: white; border-radius: 10px; overflow: hidden; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background: #3498db; color: white; }
        .stats { display: flex; gap: 20px; margin: 20px 0; }
        .card { background: white; padding: 20px; border-radius: 10px; flex: 1; text-align: center; }
        .card .value { font-size: 28px; color: #3498db; }
        .chart { text-align: center; margin: 30px 0; }
        img { max-width: 100%; }
        button { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
<div class="container">
    <h1>📊 Анализ доходов компании</h1>
    <div class="menu">
        <a href="/">🏠 Все записи</a>
        <a href="/search">🔍 Поиск</a>
        <a href="/stats">📈 Статистика</a>
        <a href="/categories">📁 Категории</a>
        <a href="/top">🏆 Топ N</a>
        <a href="/pandas">🐼 Pandas</a>
        <a href="/numpy">🔢 NumPy</a>
        <a href="/charts">📊 Графики</a>
    </div>
    <hr>
    {% block content %}{% endblock %}
</div>
</body>
</html>
'''

def get_df():
    conn = get_connection()
    records = get_all_records(conn)
    conn.close()
    return pd.DataFrame(records, columns=['id', 'company_name', 'revenue_amount', 'revenue_date', 'category', 'region'])

@app.route('/')
def index():
    conn = get_connection()
    records = get_all_records(conn)
    conn.close()
    content = '<h2>Все записи</h2><p>Всего: {}</p><table border="1"><tr><th>ID</th><th>Компания</th><th>Сумма</th><th>Дата</th><th>Категория</th><th>Регион</th></tr>'.format(len(records))
    for r in records:
        content += f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]:,.2f}</td><td>{r[3]}</td><td>{r[4]}</td><td>{r[5]}</td></tr>'
    content += '</table>'
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/search')
def search():
    company = request.args.get('company', '')
    conn = get_connection()
    records = find_by_filter(conn, company) if company else []
    conn.close()
    content = f'''
    <h2>Поиск по компании</h2>
    <form method="get"><input name="company" placeholder="Название компании" value="{company}"><button>Найти</button></form>
    '''
    if company:
        content += f'<p>Найдено: {len(records)}</p>'
        if records:
            content += '<table border="1"><tr><th>ID</th><th>Компания</th><th>Сумма</th><th>Дата</th><th>Категория</th><th>Регион</th></tr>'
            for r in records:
                content += f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]:,.2f}</td><td>{r[3]}</td><td>{r[4]}</td><td>{r[5]}</td></tr>'
            content += '</table>'
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/stats')
def stats():
    conn = get_connection()
    avg = get_average_value(conn)
    records = get_all_records(conn)
    totals = [r[2] for r in records]
    total = sum(totals)
    max_val = max(totals) if totals else 0
    min_val = min(totals) if totals else 0
    std = np.std(totals) if totals else 0
    conn.close()
    content = f'''
    <h2>Статистика</h2>
    <div class="stats">
        <div class="card"><h3>Средняя выручка</h3><div class="value">{avg:,.2f} ₽</div></div>
        <div class="card"><h3>Общая выручка</h3><div class="value">{total:,.2f} ₽</div></div>
        <div class="card"><h3>Количество записей</h3><div class="value">{len(records)}</div></div>
    </div>
    <div class="stats">
        <div class="card"><h3>Максимум</h3><div class="value">{max_val:,.2f} ₽</div></div>
        <div class="card"><h3>Минимум</h3><div class="value">{min_val:,.2f} ₽</div></div>
        <div class="card"><h3>Стандартное отклонение</h3><div class="value">{std:,.2f} ₽</div></div>
    </div>
    '''
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/categories')
def categories():
    conn = get_connection()
    report = get_group_report(conn)
    conn.close()
    content = '<h2>Отчёт по категориям</h2><table border="1"><tr><th>Категория</th><th>Количество</th></tr>'
    for r in report:
        content += f'<tr><td>{r[0]}</td><td>{r[1]}</td></tr>'
    content += '</table>'
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/top')
def top():
    limit = request.args.get('limit', 3)
    try:
        limit = int(limit)
    except:
        limit = 3
    conn = get_connection()
    records = get_top_records(conn, limit)
    conn.close()
    content = f'''
    <h2>Топ-{limit} по выручке</h2>
    <form method="get"><input name="limit" value="{limit}"><button>Показать</button></form>
    <table border="1"><tr><th>Компания</th><th>Выручка</th></tr>
    '''
    for r in records:
        content += f'<tr><td>{r[0]}</td><td>{r[1]:,.2f} ₽</td></tr>'
    content += '</table>'
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/pandas')
def pandas_analysis():
    df = get_df()
    summary = df.groupby('company_name')['revenue_amount'].agg(['sum', 'mean', 'count']).round(2)
    content = '<h2>Pandas анализ</h2><table border="1"><tr><th>Компания</th><th>Общая выручка</th><th>Средняя</th><th>Кол-во</th></tr>'
    for company, row in summary.iterrows():
        content += f'<tr><td>{company}</td><td>{row["sum"]:,.2f}</td><td>{row["mean"]:,.2f}</td><td>{row["count"]}</td></tr>'
    content += '</table>'
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/numpy')
def numpy_analysis():
    df = get_df()
    revenues = df['revenue_amount'].values
    content = f'''
    <h2>NumPy анализ</h2>
    <div class="stats">
        <div class="card"><h3>Среднее</h3><div class="value">{np.mean(revenues):,.2f} ₽</div></div>
        <div class="card"><h3>Медиана</h3><div class="value">{np.median(revenues):,.2f} ₽</div></div>
        <div class="card"><h3>Стандартное отклонение</h3><div class="value">{np.std(revenues):,.2f} ₽</div></div>
    </div>
    <div class="stats">
        <div class="card"><h3>Дисперсия</h3><div class="value">{np.var(revenues):,.2f}</div></div>
        <div class="card"><h3>Мин</h3><div class="value">{np.min(revenues):,.2f} ₽</div></div>
        <div class="card"><h3>Макс</h3><div class="value">{np.max(revenues):,.2f} ₽</div></div>
    </div>
    '''
    return HTML.replace('{% block content %}{% endblock %}', content)

@app.route('/charts')
def charts():
    df = get_df()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    df.groupby('company_name')['revenue_amount'].sum().plot(kind='bar', color='#3498db', ax=ax)
    ax.set_title('Выручка по компаниям')
    ax.set_ylabel('Выручка (₽)')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    chart = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    df.groupby('category')['revenue_amount'].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax2)
    ax2.set_title('Распределение по категориям')
    ax2.set_ylabel('')
    
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png', bbox_inches='tight')
    buf2.seek(0)
    chart2 = base64.b64encode(buf2.read()).decode('utf-8')
    plt.close(fig2)
    
    content = f'''
    <h2>Графики</h2>
    <div class="chart"><h3>Выручка по компаниям</h3><img src="data:image/png;base64,{chart}"></div>
    <div class="chart"><h3>Распределение по категориям</h3><img src="data:image/png;base64,{chart2}"></div>
    '''
    return HTML.replace('{% block content %}{% endblock %}', content)

if __name__ == '__main__':
    app.run(debug=True)