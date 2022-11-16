import random
from worker_matriz import worker

def gerar_matriz():
    matriz = []
    for i in range(1):
        linha = []
        for j in range(10):
            linha.append(random.randint(1, 100))
        matriz.append(linha)
    return matriz

def checar_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento == 0:
                print('Multiplicação falhou!')
    return print('Multiplicação bem sucedida!')

if __name__ == '__main__':
    matriz = gerar_matriz()
    for linha in matriz:
        print(linha)

