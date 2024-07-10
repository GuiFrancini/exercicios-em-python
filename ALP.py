matriz = [ [0 for i in range(3)] for a in range(3)]
i=0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = i
        i += 1

for linha in range(3):
    for coluna in range(3):
        print("%3d" % matriz[linha][coluna], end="")
    