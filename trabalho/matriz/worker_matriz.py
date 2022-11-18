import threading
import random

def worker(matrizX,matrizY,matriz_resultante,i,j):
    worker_name = threading.current_thread().name

    matriz_resultante[i][j] += matrizX[i][j] * matrizY[i][j]
    
def worker_gerar_matriz(matriz,tam_matriz):
    worker_name = threading.current_thread().name
    print('Worker: %s' % worker_name)
    for i in range(tam_matriz):
        linha = []
        for j in range(tam_matriz):
            linha.append(random.randint(1, 10))
        matriz.append(linha)
    return matriz
