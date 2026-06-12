def get_all_records(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM revenues")
    return cursor.fetchall()


def find_by_filter(connection, company_name):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM revenues WHERE company_name = ?", (company_name,))
    return cursor.fetchall()


def get_top_records(connection, limit=3):
    cursor = connection.cursor()
    cursor.execute("SELECT company_name, revenue_amount FROM revenues ORDER BY revenue_amount DESC LIMIT ?", (limit,))
    return cursor.fetchall()