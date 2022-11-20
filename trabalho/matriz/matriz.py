from worker import worker_multiplica_matriz, worker_gerar_matriz
from concurrent.futures import ThreadPoolExecutor

WORKERS=10

def gerar_matriz():
    matriz = []
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        executor.submit(worker_gerar_matriz(matriz,1000))
        
    executor.shutdown()
    return matriz


def checar_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento == 0 or elemento == None:
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
        
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        for i in range(len(matrizX)):
            for j in range(len(matrizY[0])):
                executor.submit(worker_multiplica_matriz,matrizX,matrizY,matriz_resultante,i,j)
                
        executor.shutdown()
    checar_matriz(matriz_resultante)
if __name__ == '__main__':
    multiplicar_matrizes()
    
    
# from math import sqrt
# from joblib import Parallel, delayed
# print(Parallel(n_jobs=10)(delayed(sqrt)(i) for i in range(10000)))