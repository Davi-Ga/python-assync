import threading
import time
from queue import Queue

def worker():
    print('Iniciando', threading.current_thread().name)
    time.sleep(2)
    print('Finalizando', threading.current_thread().name)
    
if __name__=='__main__':
    threads=[]
    for i in range(5):
        t=threading.Thread(target=worker)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        