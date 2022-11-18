from time import sleep 
from threading import *

global x
x = 2

class SomaWorker(Thread): #Worker de somatorio 
    def run(self):
        x0 = x
        for i in range(10):
            x0+=1
            print(x0)
            print(x)
        return x0




class SubWorker(Thread):
    def run(self):
        x = 0
        for i in range(10):
            x-=1
            print(x)
        return x


t1 = SomaWorker() #Instancia os Workers em uma variavel

t2 = SubWorker()


t1.start() #Starta o worker
sleep(0.2)
t2.start()

t1.join() #Inicia a execução do Worker
# t2.join()


print('Bye')
