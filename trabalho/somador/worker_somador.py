from time import sleep 
from threading import *

global x
x = 0
class SomaWorker(Thread): #Worker de somatorio
    
    def run(self):
        global x
        for i in range(100):
            x+=1
            print(x)
            




class SubWorker(Thread):

    def run(self):
        global x
        for i in range(100):
            x-=1
            print(x)

    

t1 = SomaWorker() #Instancia os Workers em uma variavel

t2 = SubWorker()


t1.start() #Starta o worker
t2.start()
t1.join() #Inicia a execução do Worker
t2.join()


print('Bye')
