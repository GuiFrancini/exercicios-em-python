#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Elabore um programa que pergunte ao usuário um número e 
# depois crie um vetor/lista com todos os divisores desse número.

numero = int(input("Digite um numero:"))
lista= []

for i in range(1,numero + 1):
    if numero % i == 0:
        lista.append(i)

print("Os divisores de",numero,"\nsão:",lista)
