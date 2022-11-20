import hashlib
from concurrent.futures import ThreadPoolExecutor


dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



#Ideia: criar um vetor de worker que receba - woker = []
# worker.push[<nome da função worker/theading>[lenght(dict)/MAXWORKERS]]


worker = []

 

hash = 'ed968e840d10d2d313a870bc131a4e2c311d7ad09bdf32b3418147221f51a6e2' #aaaaa


def crack(str):
    global dict
    for i in range (26):
        for j in range(26):
            for k in range (26):
                for l in range(26):
                        str.append(dict[i])
                        str.append(dict[j])
                        str.append(dict[k])
                        str.append(dict[l])

                        hashB = hashlib.sha256(''.join(str).encode())
                        resultB = hashB.hexdigest()
                        
                        if(hash == resultB):
                            print("Achei")
                            print(f"A palavra decodificada é: {''.join(str)}")
                        print(str)
                        str.pop()
                        str.pop()
                        str.pop()
                        str.pop()
                        

i = 0 #Worker 1 
j = 0 #Worker 2
k = 0 #Worker 3
l = 0 #Worker 4


letra = []
worker.append(dict[0])
WORKERS = 10 #Passar isso para os workers
def gerar_matriz():
    global letra
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        for cont in range(len(dict)):
            letra.append(dict[cont])
            executor.submit(crack(letra))
            letra.pop()

gerar_matriz()
