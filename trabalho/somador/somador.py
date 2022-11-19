from worker_somador import *

t1 = SomaWorker() #Instancia os Workers em uma variavel

t2 = SubWorker()


t1.start() #Starta o worker
t2.start()
t1.join() #Inicia a execução do Worker
t2.join()


print('Bye')
