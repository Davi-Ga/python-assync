from worker import worker_multiplica_matriz, worker_gerar_matriz
from concurrent.futures import ThreadPoolExecutor

WORKERS=1

def gerar_matriz():
    matriz = []
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.submit(worker_gerar_matriz(matriz,10))
    
    executor.shutdown()
    
    return matriz

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
        executor.submit(worker_multiplica_matriz,matrizX,matrizY,matriz_resultante,i,j)
                
        executor.shutdown()
    print('Matriz Calculada!')
if __name__ == '__main__':
    multiplicar_matrizes()
    
    
# from math import sqrt
# from joblib import Parallel, delayed
# print(Parallel(n_jobs=10)(delayed(sqrt)(i) for i in range(10000)))