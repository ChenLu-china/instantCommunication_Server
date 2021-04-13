import json
import socket
import time

MaxBytes = 1024 * 1024
host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect((host, port))
time.sleep(5)
msg1 = {'head': 'login', 'user_name': "ChenLu", 'user_password': "cl961007"}
jmsg1 = json.dumps(msg1)
s.send(jmsg1.encode('utf-8'))
receive_msg = s.recv(MaxBytes)


print(receive_msg.decode('utf-8'))

