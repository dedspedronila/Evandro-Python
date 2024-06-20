num = [0]*6
cont = 0

for cont in range(0,6,1):
    print("Por favor, preencha os números com numeros positivos e negativos")
    num[cont] = int(input(f"Informe um valor para ser armazenado na posição {cont+1}: "))

for cont in range(6):
    if(num[cont] > 0):
        num[cont] = 1
    else:
        num[cont] = 0
    
    print(f"Os valores substituidos ficaram: {num[cont]}")