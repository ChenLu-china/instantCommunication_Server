import socket
import threading
import json
from service import LoginService
from concurrent_collection.cQueue import ConcurrentQueue
from global_param.params import session_user_map, user_msgq_map
import time
import uuid
import threading


max_bytes = 1024 * 1024
bind_address = '127.0.0.1'
bind_port = 8888
auth_lock = threading.Lock()


def start_server():
    '''
        Should be run in a thread. When a new connection is accpeted, start timer for auth.
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((bind_address, bind_port))
    print('ready to connect to client')
    s.listen(10)
    while True:
        sock, addr = s.accept()
        # create a threading to deal with TCP 连接
        t = threading.Thread(target=main_function, args=(sock, addr))
        t.start()
    

def main_function(sock, addr):

    
    flag, msgQ, session_id = auth(sock, addr)
    
    # 死循环从队列里面获取消息回写给客户端
    while flag:
        if msgQ.empty():
            continue

        msg_bytes = msgQ.poll()
        # 如果消息为 close，解除引用，并终止循环（线程）
        if msg_bytes.decode() == 'close':
            username = session_user_map.pop(session_id)
            q_list = user_msgq_map.get(username)
            # 此次要用和写入队列一样的锁
            q_list.remove(msgQ)
            break

        socket_send(sock, msg_bytes)
        



        


def auth(sock, addr):
    sock.setblocking(0) # 设置非阻塞
    time_start = time.time()
    while True:
        # Auth timeout 3 s
        if time.time() - time_start > 3:
            print("connectiong timeout")
            sock.close()
            break
        # 非阻塞式接受消息
        try:
            recv_bytes = sock.recv(max_bytes)
        except BlockingIOError as e:
            recv_bytes = None

        # 无消息则继续循环，消息长度为0则断开连接
        if recv_bytes == None:
            continue
        elif len(recv_bytes) == 0:
            sock.close()
            break
        
        json_obj = json.loads(recv_bytes.decode('utf-8'))
        # 如果不是 login，不合法，关闭连接
        if json_obj['head'] != 'login':
            sock.close()
            break

        print(f"this is the request of {addr}")
        if LoginService.deal_login(json_obj):
            # 登录成功创建消息队列
            msgQ = ConcurrentQueue()

            auth_lock.acquire()
            try:
                # 放进全局变量 map 里面
                q_list = user_msgq_map.get(json_obj['user_name'])
                if None == q_list:
                    q_list = []
                    user_msgq_map[json_obj['user_name']] = q_list
                q_list.append(msgQ)
            finally:
                auth_lock.release()

            # 发送通讯录和会话ID
            session_id = str(uuid.uuid1()).replace("-", "")
            # session id 放进全局变量 map 里面
            session_user_map[session_id] = json_obj['user_name']

            receivers_list = LoginService.get_communication_list(json_obj['user_name'])
            msg = json.dumps({"session_id": session_id, "receivers": receivers_list}).encode('utf-8')
            # 将消息塞入队列
            msgQ.offer(msg)
            return True, msgQ, session_id
            
    
    return False, None, None


# 发送失败 要异常捕获，待处理
def socket_send(target_sock, bytes):
    target_sock.send(bytes)
