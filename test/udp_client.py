import socket
import json

target_ip = '159.75.220.96'
# target_ip = '127.0.0.1'
target_port = 7777

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

session_id = input("session id: ")

while True:
    message = input("your message: ")
    data = {
        "type": "text",
        "to": "ChenLu",
        "session": session_id,
        "message":message
    }

    client_socket.sendto(json.dumps(data).encode('utf-8'), (target_ip, target_port))