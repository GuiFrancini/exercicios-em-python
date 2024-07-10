#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Elabore um programa que preencha automaticamente um vetor numérico com 50 números 
# e depois separe-os para outros dois vetores entre números vetorpar e ímpares.
# Ao final, mostre os três vetores.

vetor = []
vetorpar = []
vetorimpar = [] 

for i in range(1, 51):
    vetor.append(i)

for i in vetor:
    if i % 2 == 0:
        vetorpar.append(i)
    else:
        vetorimpar.append(i)

print("Vetor",vetor)
print("Veror par:",vetorpar)
print("Vetor impar",vetorimpar)