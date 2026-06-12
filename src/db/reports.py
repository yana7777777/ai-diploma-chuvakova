def get_average_value(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(revenue_amount) FROM revenues")
    return cursor.fetchone()[0]


def get_group_report(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT category, COUNT(*) FROM revenues GROUP BY category")
    return cursor.fetchall()