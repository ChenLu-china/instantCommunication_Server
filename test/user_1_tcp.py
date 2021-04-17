import json
import socket
import time

MaxBytes = 1024 * 1024
host = '159.75.220.96'
# host = '127.0.0.1'
port = 8888

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect((host, port))
msg1 = {'head': 'login', 'user_name': "ChenLu", 'user_password': "cl961007"}
jmsg1 = json.dumps(msg1)

print("login json >>> ", jmsg1)
print('try login ...')

s.send(jmsg1.encode('utf-8'))
while True:
    receive_msg = s.recv(MaxBytes)
    print("receive msg >>> ", receive_msg.decode('utf-8'))

