from worker import worker_subtrai, worker_somador
from concurrent.futures import ThreadPoolExecutor

WORKERS=10
count = 0
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        executor.submit(worker_subtrai,200000000)
        executor.submit(worker_somador,200000000)
        
        
        executor.shutdown()
        
    


print('Bye')
