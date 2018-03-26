# 不加锁测试
'''
    Lock也可以叫做互斥锁，其实相当于信号量为1。一个不加锁的例子：
'''

import time
import threading

value = 0

def getlock():
    global value
    new = value + 1
    time.sleep(0.001)   #让线程有机会切换
    value = new

for i in range(100):
    t = threading.Thread(target=getlock)
    t.start()

main_thread = threading.current_thread()

for t in threading.enumerate():
    if t == main_thread:
        continue
    t.join()

print(value)