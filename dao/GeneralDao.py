import pymysql

host = '172.16.0.8:3306'
port = 3306

def create_MySql_Connection():
    conn = pymysql.connect(
        host=host,
        port = port,
        user='root',
        password='Abcd123456',
        db='im',
        charset='utf8'
    )
    return conn