import random
from worker_matriz import worker
from concurrent.futures import ThreadPoolExecutor
import threading

def gerar_matriz():
    matriz = []
    for i in range(1000):
        linha = []
        for j in range(1000):
            linha.append(random.randint(1, 10))
        matriz.append(linha)
    return matriz

def checar_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento == 0:
                print('Multiplicação falhou!')
    return print('Multiplicação bem sucedida!')


def multiplicar_matrizes():
    matrizX = gerar_matriz()
    matrizY = gerar_matriz()
    matriz_resultante = []
    for i in range(len(matrizX)):
        linha = []
        for j in range(len(matrizX)):
            linha.append(0)
        matriz_resultante.append(linha)
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(len(matrizX)):
            for j in range(len(matrizY[0])):
                executor.submit(worker(matrizX,matrizY,matriz_resultante,i,j))

    for linha in matriz_resultante:
        print(linha)
if __name__ == '__main__':
    multiplicar_matrizes()