linha = 0
coluna = 0
matriz = [
    [0]*3,
    [0]*3,
    [0]*3,
]

for linha in range(0,3,1):
    for coluna in range(0,3,1):
        matriz[linha][coluna] = int(input(f"Informe um valor para a posição {linha+1}|{coluna+1}: "))

for linha in range(0,3,1):
    for coluna in range(0,3,1):
        print(f"[{matriz[linha][coluna]}]", end =' ')
    print()