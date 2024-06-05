num = int(input("Informe um número: "))
maior = num
menor = num

while num != 0:
    if(num > maior):
        maior = num
    else:
        if(num < menor) and (num !=0):
            menor = num
    
    num = int(input("Informe um número: "))
    

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi> {menor}")
