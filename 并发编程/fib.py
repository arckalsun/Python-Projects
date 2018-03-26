
# 计算型任务
# 结果是nothread耗时少，因为GIL会让多线程变慢
import time
import threading

def text(name):
    def profile(func):
        def wrapper(*args,**kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            end = time.time()
            print('{} cost:{}'.format(name,end-start))
            return res
        return wrapper
    return profile

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

@text('nothread')
def nothread():
    fib(35)
    fib(35)

@text('hasthread')
def hasthread():
    for i in range(2):
        t = threading.Thread(target=fib,args=(35,))
        t.start()
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        print(t)
        if t is main_thread:
            continue
        t.join()

if __name__ == '__main__':
    nothread()
    hasthread()