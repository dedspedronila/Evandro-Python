linha = 0
coluna = 0
matriz = [
    [0.0]*3,
    [0.0]*3,
]

for linha in range(0,2,1):
    for coluna in range(0,3,1):
        matriz[linha][coluna] = float(input(f"Informe o valor para a posição {linha+1}|{coluna+1}: "))
print("Aqui será exibido a Matriz Original")
for linha in range(0,2,1):
    for coluna in range(0,3,1):
        print(f"[{matriz[linha][coluna]}]", end=' ')
    print()

print("Aqui será exibido a Matriz Transposta")


for linha in range(0,3,1):
    for coluna in range(0,2,1):
        print(f"[{matriz[coluna][linha]}]", end =' ')
    print()