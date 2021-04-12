import json
import socket
import time

MaxBytes = 1024 * 1024
host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect((host, port))
while True:
    msg1 = [{'head': 'login', 'user_name': "ChenLu", 'user_password': "cl961007"}]
    jmsg1 = json.dumps(msg1)
    s.send(jmsg1.encode())
    receive_msg = s.recv(MaxBytes)
    if not receive_msg:
        print("Received message is empty...........")
        break
    localTime = time.asctime(time.localtime(time.time()))
    print(localTime, "Received message length is", len(receive_msg))
    print("Server said to you:", receive_msg.decode())
s.close()
print("Client has been closed.................")
