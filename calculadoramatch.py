#AUTHOR: GUILHERME FRANCINI
#DESCRIPTION: CALCULATOR IN PYTHON
#DATE: 06/05/2024
#calculadora usando o match case
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Não é possível dividir por zero!"
    else:
        return x / y

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = match escolha:
    case '1':
        adicao(num1, num2)
    case '2':
        subtracao(num1, num2)
    case '3':
        multiplicacao(num1, num2)
    case '4':
        divisao(num1, num2)
    case _:
        "Escolha inválida"

print("Resultado:", resultado)
