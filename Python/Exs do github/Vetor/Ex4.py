num = [0]*50
cont = 0

for cont in range(0,50,1):
    num[cont] = float(input(f"Informe o valor para a posição {num[cont+1]}: "))
    if(num[cont] % 2 == 0):
        num[cont] = num[cont] *1.02
        
    else:
        num[cont] = num[cont] *1.05
        
print("O vetor com os aumentos, ficará: ")
for cont in range(0,50,1):
    print(f"{num[cont]:,.2f}" , end=' ')
