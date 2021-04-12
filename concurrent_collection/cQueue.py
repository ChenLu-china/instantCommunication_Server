import queue
import threading

class ConcurrentQueue:

    def __init__(self):
        self.__mutex = threading.Lock() #不可重入锁
        self.__cond = threading.Condition(self.__mutex) # 初始化条件变量
        self.__queue = queue.Queue()    #初始化队列

    def poll(self):
        self.__cond.acquire()

        try:
            elem = self.__queue.get_nowait()
            return elem
        except queue.Empty as e:
            return None
        finally:
            self.__cond.release()

    def offer(self, elem):
        self.__cond.acquire()

        try:
            self.__queue.put(elem)
        finally:
            self.__cond.release()

    def empty(self):
        return self.__queue.empty()