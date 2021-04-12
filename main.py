# This is a sample Python script.
import socket as skt
import threading

import MainFunction


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def start_server():
    s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
    s.bind(('127.0.0.1', 8888))
    print('ready to connect to client')
    s.listen(10)
    while True:
        sock, addr = s.accept()
        # create a threading to deal with TCP 连接
        t = threading.Thread(target=MainFunction.main_function, args=(sock, addr))
        t.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_server()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
