import json

import pymysql


def deal_login(jason_data):
    conn = create_MySql_Connection()
    user_name, user_password = deal_jason(jason_data)
    check_result = check_userinfo(conn, user_name, user_password)

    if check_result:
        list_name = get_communication_list(conn, user_name)
        conn.close()
        return list_name
    else:
        conn.close()
        return "This user is not available!"


def check_userinfo(conn, user_name, user_password):
    cursor = conn.cursor()
    check_result = bool
    sql = "SElECT user_name, user_password \
            from users \
            where \
            users.user_name = '%s' \
            and user_password = '%s' " % (user_name, user_password)
    num_ = cursor.execute(sql)

    if num_ == 1:
        check_result = True
    elif num_ == 0:
        check_result = False
    cursor.close()
    return check_result


def create_MySql_Connection():
    conn = pymysql.connect(
        # host='localhost',
        # port = 3306,
        user='root',
        password='cl961007',
        db='User',
        charset='utf8'
    )
    return conn


def close_MySql_connection(conn):
    conn.close()


def deal_jason(json_data):
    user_name = json_data[0]['user_name']
    user_password = json_data[0]['user_password']
    return user_name, user_password


def get_communication_list(conn, user_name):
    cursor = conn.cursor()
    sql = "select * from co_list where sender = '%s'" % user_name
    cursor.execute(sql)
    communication_list = {}
    receives = []
    titles = []
    data = cursor.fetchall()
    fields = cursor.description
    for i in fields:
        titles.append(i[0])
    for row in data:
        result = {titles[1]: row[1]}
        receives.append(result)
    print(communication_list)
    communication_list = {user_name: receives}
    communication_list = json.dumps(communication_list)
    cursor.close()
    return communication_list
