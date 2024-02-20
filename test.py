#2023/10/19
import threading
import time

def worker():
  count = 0
  while True:
    time.sleep(1)
    count = count + 1 
    print("我是线程Thread-1")
    if count == 3:
      print("Thread-1退出")
      break
  
def worker5():
  time.sleep(10)
  print("Thread-3退出")
  
def worker2():
   t3 = threading.Thread(target=worker5, name="Thread-3")
   t3.start()
   time.sleep(1)
   print("Thread-2退出")

def work_daemon():
  while True:
    print([i.name for i in threading.enumerate()])
    time.sleep(1)

t1 = threading.Thread(target=worker, name="Thread-1")
t2 = threading.Thread(target=worker2, name="Thread-2")
t3 = threading.Thread(target=work_daemon, name="Thread-daemon")

t1.start()
t2.start()
t3.setDaemon(True)#设置t3为守护线程
t3.start()
print("主线程运行结束")#运行结束并不意味着退出
#输出：
"""
['MainThread', 'Thread-1', 'Thread-2', 'Thread-daemon']
主线程运行结束
Thread-2退出
我是线程Thread-1
['MainThread', 'Thread-1', 'Thread-daemon']
我是线程Thread-1
['MainThread', 'Thread-1', 'Thread-daemon']
我是线程Thread-1
Thread-1退出

守护线程之所以叫“守护”是因为该线程通常用于为其他线程提供服务，或监控其他线程等，
例如守护线程监测到某线程异常退出后可以重新创建该线程。因为服务于进程内的所有线程，
所以守护线程一般是一个死循环，所有线程结束后守护线程才会自动退出循环，退出线程。
值得注意的是线程运行结束不意味着线程退出，比如观察图二代码的图三输出，图三输出显示主线程运行结束后并没有退出，
主线程需要其他所有非守护线程退出后才退出，主线程退出后守护线程退出
"""
