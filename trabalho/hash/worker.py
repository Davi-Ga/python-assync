import hashlib
from concurrent.futures import ThreadPoolExecutor
import sys
import threading

dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 
def worker(letra):
    hash = '5e846c64f2db12266e6b658a8e5b5b42cc225419b3ee1fca88acbb181ddfdb52'
    global flag
    for i in dict:
        for j in dict:
            for k in dict:
                for l in dict:
                    palavra = letra + i + j + k + l
                    
                    if hashlib.sha256(palavra.encode('utf-8')).hexdigest() == hash:
                        print('Palavra encontrada: ' + palavra)
                        print('Fim')
                        print("Finalizado thereads ...")
                        flag = 1
                        return  

flag = 0


with ThreadPoolExecutor(max_workers=26) as executor:
    flag = 0
    for i in dict:
        executor.submit(worker,i)

        if flag == 1:
            exit()  

    executor.shutdown(wait=True)




# test = 'bbbbb'
# print(hashlib.sha256(test.encode('utf-8')).hexdigest())
