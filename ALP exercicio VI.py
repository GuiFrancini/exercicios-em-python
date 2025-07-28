#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Crie uma matriz F 3x3 com números aleatórios entre 1 e 5.
# Calcule e mostre na tela:
# 1 – Divisão de todos os elementos da linha 0 por 2;
# 2 – Multiplicação de todos os elementos da coluna 2.
# 3 - Soma de todos os valores da matriz.
import random
matriz = [[random.randint(1, 5) for i in range(3)] for i in range(3)]

print("Matriz")
for i in matriz:
    print(i)

linhaD = [i / 2 for i in matriz[0]]
print("Divisão dos elementos da linha 0")
print(linhaD)


coluna2 = [coluna[2] for coluna in matriz]
colunaM = [i* i for i in coluna2]
print("Multiplicação de todos os elementos da coluna 2:")
print(colunaM)

coluna = sum(sum(matriz) for matriz in matriz)
print("Soma dos valores da matriz")
print(coluna)

