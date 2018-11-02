import time
import threading
def Scheduler(task_function_list):
    tasks=[]
    for i,(func,delay) in enumerate(task_function_list):
        t = threading.Thread(target=_Scheduler, args=(i,func,delay/1000))
        t.start()
        tasks.append(t)
        
    tasks[-1].join()
    
    

def _Scheduler(number,task_function, duration):
    init_time = time.time()
    time.sleep(duration)
    if time.time()-init_time >= duration:
        task_function()
        print("Thread {} Called, delay duration:{}".format(number, duration))
#         break

def task():
    print("Myah")

if __name__ == '__main__':
    print("calling")
    task_list=[(task,2000),(task,200),(task,2)]
    Scheduler(task_list)
