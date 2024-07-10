
#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Escreva um programa que leia o valor de um boleto e quantos dias de atraso.
#Caso haja atraso uma multa de 10% será aplicada no valor do boleto e R$2,00/dia de atraso.
#Mostre ao usuário o total a pagar.

valor = int(input("Digite o valor do boleto"))
dias = int(input("Digite o numero de dias de atraso"))
multa=0

if dias >= 1:
    multa = valor * 0.1
    dias = dias * 2
    valor = multa + dias + valor

    print("Valor total a pagar:",valor)

else:
    print("seu boleto não contem pendencias")