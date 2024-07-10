#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Escreva um programa que leia o valor de um boleto e quantos dias de atraso.
#Caso haja atraso uma multa de 7.5% será aplicada no valor do boleto e R$0,75/dia de atraso.
#Mostre ao usuário a seguinte mensagem: "Você atrasou x dias. O valor total a pagar é y. ".

valor = float(input("Digite o valor do boleto"))
dias = int(input("Digite o numero de dias de atraso"))
multa=0
multadia=0
valortotal=0

if dias >= 1:
    multa = valor * 0.075
    multadia = dias * 0.75
    valortotal = multa + multadia + valor

    print("Você atrasou",dias,f"dias. O valor total a pagar é: {round(valortotal, 2)}")

else:
    print("seu boleto não contem pendencias")