# 信号量测试
'''
    在多线程编程中，为了防止不同的线程同时对一个公用的资源（如全局变量）进行修改，
    需要进行同时访问的数量限制（通常是1）。信号量同步基于内部计数器，
    每调用一次acquire()，计数器减1；每调用一次release()，计数器加1。
    当计数器为0时，acquire()调用被阻塞。
'''

import  time
from random import random
from threading import Thread,Semaphore,current_thread,enumerate

sema = Semaphore(3)

def foo(tid):
    with sema:
        print('{} acquire sema'.format(tid))
        wt = random() * 2
        time.sleep(wt)
    print('{} release sema'.format(tid))

if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=foo,args=(i,))
        t.start()
    main_thread = current_thread()

    for t in enumerate():
        if t is main_thread:
            continue
        t.join()