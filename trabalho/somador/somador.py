from worker import worker_subtrai
from concurrent.futures import ThreadPoolExecutor

WORKERS=10


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        for i in range(20000):
            executor.submit(worker_subtrai(i))
        
        executor.shutdown()
        
    


print('Bye')
