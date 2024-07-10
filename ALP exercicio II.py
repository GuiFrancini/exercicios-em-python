#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION:algoritmo que se a idade digitada pelo usuario for menor que 16, entre 17 e 18 e acima de 18 exibe uma mensagem

nome = input("Qual é seu nome?")
idade = int(input("Qual é a sua idade?"))
acompanhada = input("Você está acompanhada?")

if idade < 16:
    print(nome,", você não pode entrar")

elif idade == 16 or idade == 17 :
    if acompanhada == "sim":
        print(nome,"Você pode entrar")
    else :
        print(nome, "Você NÃO pode entrar!!!")
elif idade >= 18:
    print(nome,"Você pode entrar")
  



    
