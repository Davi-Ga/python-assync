import threading

def worker(matrizX,matrizY,matriz_resultante,i,j):
    worker_name = threading.current_thread().name

    matriz_resultante[i][j] += matrizX[i][j] * matrizY[i][j]

