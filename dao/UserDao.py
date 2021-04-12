from dao.GeneralDao import create_MySql_Connection

def check_user_info(username, password):
    conn = create_MySql_Connection()
    cursor = conn.cursor()
    try:
        if username != None and password != None and len(username) > 0 and len(password) > 0:
            sql = "SElECT user_name, user_password \
                    from users \
                    where \
                    users.user_name = '%s' \
                    and user_password = '%s' " % (username, password)
            num_ = cursor.execute(sql)

            if num_ == 1:
                return True
        
        return False
    finally:
        cursor.close()
        conn.close()

    
