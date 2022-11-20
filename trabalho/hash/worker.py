import hashlib
from concurrent.futures import ThreadPoolExecutor
import sys

dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
 

 #aaaaa
def close():
    print('Fim')
    sys.exit()

def worker(letra):
    hash = '5e846c64f2db12266e6b658a8e5b5b42cc225419b3ee1fca88acbb181ddfdb52'
    for i in dict:
        for j in dict:
            for k in dict:
                for l in dict:
                    palavra = letra + i + j + k + l
                    if hashlib.sha256(palavra.encode('utf-8')).hexdigest() == hash:
                        print('Palavra encontrada: ' + palavra)
                        close() # procurar um jeito de finaliza a thread de forma assincrona


with ThreadPoolExecutor(max_workers=5) as executor:
    for i in dict:
        executor.submit(worker,i)

    executor.shutdown(wait=True)


print('Fim')


# test = 'bbbbb'
# print(hashlib.sha256(test.encode('utf-8')).hexdigest())
