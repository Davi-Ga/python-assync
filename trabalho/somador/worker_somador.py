from time import sleep 
from threading import *

global x
x = 0
class SomaWorker(Thread): #Worker de somatorio
    
    def run(self):
        global x
        for i in range(10000):
            x+=1
            print(x)


class SubWorker(Thread):

    def run(self):
        global x
        for i in range(10000):
            x-=1
            print(x)

    


