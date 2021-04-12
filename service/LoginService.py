from dao import UserDao
from dao import CoListDao


def deal_login(json_data):
    flag = UserDao.check_user_info(json_data['user_name'], json_data['user_password'])

    if not flag:
        print("No user info or wrong password")

    return flag


def get_communication_list(user_name):
    return CoListDao.get_communication_list(user_name)
