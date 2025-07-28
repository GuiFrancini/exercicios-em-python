#AUTHOR: GUILHERME FRANCINI
#DATE: 06/05/2024
#DESCRIPTION: Antônio irá tirar sua habilitação, porém a legislação só permite o início nas aulas prática, após ele passar no exame psicotécnico, médico e teórico. Escreva um programa que após as entradas dos resultados de todos os exames citados, informe se Antônio está apto ou não a iniciar as aulas práticas.
# Simule um ambiente onde o Antônio não passou na prova teórica.

psico = input("qual é o resultado do teste psicotécnico? (responda com positivo ou negativo)")
medico = input("qual é o resultado do teste médico? (responda com positivo ou negativo)")
teorico = input("qual é o resultado do teste teórico? (responda com positivo ou negativo)")

if psico == "positivo" and medico =="positivo" and teorico =="positivo":
    print("Antonio está apto para as aulas praticas")
else:
    print("antonio NÃO está apto")
    
