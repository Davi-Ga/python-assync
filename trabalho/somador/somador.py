from worker import worker_subtrai, worker_somador
from concurrent.futures import ThreadPoolExecutor

WORKERS=10
count  = 20000

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        executor.submit(worker_subtrai,count)
        executor.submit(worker_somador,count)
        
        
        executor.shutdown()
        
    


print('Bye')
