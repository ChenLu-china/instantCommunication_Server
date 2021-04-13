import pymysql

host = '172.16.0.8'
port = 3306
# host = 'gz-cdb-7fa8sxrh.sql.tencentcdb.com'
# port = 58915

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