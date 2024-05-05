import threading  
import time  
from threading import Event  
  
def worker(event, name, should_wait=False):  
    if should_wait:  
        print(f"{name,threading.current_thread().ident } 阻塞等待...")  
        event.wait()  # 等待事件被设置  
        print(f"{name,threading.current_thread().ident } 解除阻塞。")  
        
    event.set()  # 设置事件，以通知其他线程，解除阻塞
   
  
def worker_thread(name, event): 
   print(f"{name,threading.current_thread().ident } 阻塞等待...")   
   event.wait()  # 等待事件被设置  
   print(f"{name,threading.current_thread().ident } 解除阻塞。")  
  
def main():  
    event = Event()  
    event_mian = Event()
      
    thread_non_waiting = threading.Thread(target=worker,
                                    args=(event, "线程-非等待"))  
    thread_waiting_for_event = threading.Thread(target=worker,
                                    args=(event, "线程-等待事件", True))    
    thread_waiting_mian_thread = threading.Thread(target=worker_thread, 
                                    args=("线程-等待主线程",event_mian,))  
      
    thread_non_waiting.start()  
    thread_waiting_for_event.start()  
    thread_waiting_mian_thread.start() 
    
    time.sleep(1)  
    event_mian.set() # 设置事件，以通知其他线程，解除阻塞
    
    thread_non_waiting.join()
    thread_waiting_for_event.join()
    thread_waiting_mian_thread.join()
    print("所有线程都已完成。")  
    
if __name__ == "__main__":  
    main()