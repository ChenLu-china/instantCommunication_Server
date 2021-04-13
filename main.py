# This is a sample Python script.
from socket_func import tcp_conn, udp_conn
import threading



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # tcp connection receiver thread
    tcp_t = threading.Thread(target=tcp_conn.start_server)
    tcp_t.start()

    # udp connection receiver thread
    udp_t = threading.Thread(target=udp_conn.start_server)
    udp_t.start()

