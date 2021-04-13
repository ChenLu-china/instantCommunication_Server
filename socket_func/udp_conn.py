import socket
from global_param.params import user_msgq_map, user_lock_map, session_user_map
import json

host_ip = "0.0.0.0"
port = 7777
max_bytes = 1024 * 1024

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host_ip, port))

    # 循环接受消息
    while True:
        msg_bytes, addr = s.recvfrom(max_bytes)
        if len(msg_bytes) == 0:
            continue
        message = msg_bytes.decode('utf-8')
        if len(message) == 0:
            continue
        try:
            obj = json.loads(message)
        except:
            print("消息JSON不合法")
            continue
        # 检查报文格式
        if 'type' not in obj.keys() or 'to' not in obj.keys() or 'message' not in obj.keys() or 'session' not in obj.keys():
            continue

        # 检查 session
        if None == obj['session'] or None == session_user_map.get(obj['session']):
            continue
        send_user = session_user_map[obj['session']]

        # 文本消息
        if obj['type'] == 'text':
            send_text(send_user, obj['to'], obj['message'])

def send_text(send_user, to_user, message):
    if len(to_user) == 0 or len(message) == 0:
        return
    # 获取对方的消息队列
    msgq = user_msgq_map.get(to_user)
    if None == msgq:
        return
    
    # 获取接收用户队列锁
    



