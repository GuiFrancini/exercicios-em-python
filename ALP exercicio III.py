#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Crie uma matriz F 3x3 com números aleatórios entre 1 e 5.
# Calcule e mostre na tela:
# 1 – Multiplicação de todos os elementos da linha 1 por 3;
# 2 – Soma de todos os elementos da coluna 2.
import random
matriz = [[random.randint(1, 5) for i in range(3)] for i in range(3)]

print("Matriz")
for i in matriz:
    print(i)

linhaM = [i * 3 for i in matriz[1]]
print("Multiplicação da linha 1")
print(linhaM)

coluna = sum(i[2] for i in matriz)
print("Soma da coluna 2")
print(coluna)
