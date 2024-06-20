num = [0] * 6
cont = 0

for cont in range(0, 6, 1):
    num[cont] = int(input(f"Escolha um numero para a posição {cont+1} :"))


for cont in range(6):
    if(num[cont] < 0):
        print (num[cont] * -1)
    elif num[cont] > 10:
        num2 = int(input("Informe um novo valor: "))
        print (num[cont] - num2)
    else:
        print (num[cont] / 5)
