# 死锁测试
'''
    死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，
    若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互
    相等待的进程称为死锁进程。
'''
import threading
import time

mutex = threading.RLock()

# mutexA = threading.Lock()
# mutexB = threading.Lock()

class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        mutex.acquire()    #如果锁被占用，则阻塞在这里，等待锁的释放
        print("I am %s, get res: %s---%s" %(self.name, "ResA",time.time()))
        mutex.acquire()  # 如果锁被占用，则阻塞在这里，等待锁的释放
        print("I am %s, get res: %s---%s" % (self.name, "ResB", time.time()))

        mutex.release()
        mutex.release()

    def fun2(self):
        mutex.acquire()  # 如果锁被占用，则阻塞在这里，等待锁的释放
        print("I am %s, get res: %s---%s" % (self.name, "ResB", time.time()))

        time.sleep(0.2)

        mutex.acquire()  # 如果锁被占用，则阻塞在这里，等待锁的释放
        print("I am %s, get res: %s---%s" % (self.name, "ResA", time.time()))

        mutex.release()
        mutex.release()

if __name__ == '__main__':
    print("start------------------------%s" % time.time())

    for i in range(0,10):
        my_thread = MyThread()
        my_thread.start()