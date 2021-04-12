import LoginSever
import json
max_bytes = 1024 * 1024


def main_function(sock, addr):
    while True:
        json_ = json.loads(sock.recv(max_bytes).decode())
        json_head = json_[0]['head']
        if json_head == "login":
            print(f"this is the request of {addr}")
            receivers_list = LoginSever.deal_login(json_)
            sock.send(receivers_list.encode())
            print('send successful')
        elif json_head == 'communication':
            print(f"this is the request of {addr}")
