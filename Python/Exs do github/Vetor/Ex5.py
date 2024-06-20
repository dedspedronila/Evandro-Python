def subst(num):
    for cont in range(30):
        if num[cont] >= 0:
            num[cont] = 1
        else:
            num[cont] = 0
    return num

num = [0]*30
for cont in range(30):
    num[cont] = int(input(f"Informe um valor na posição {cont+1}: "))

print(num)

subst(num)

print(num)
