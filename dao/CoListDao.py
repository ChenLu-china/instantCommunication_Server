from dao.GeneralDao import create_MySql_Connection


def get_communication_list(user_name):
    conn = create_MySql_Connection()
    cursor = conn.cursor()
    try:
        sql = "select * from co_list where sender = '%s'" % user_name
        cursor.execute(sql)
        data = cursor.fetchall()

        receives = [row[1] for row in data]
        return receives
    finally:
        cursor.close()
        conn.close()