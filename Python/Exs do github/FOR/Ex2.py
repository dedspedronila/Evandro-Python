idade_soma = 0
idade_maior = 0
idade_menor = 0
idade_media = 0.0
num = int(input("Informe o número de pessoas: "))


for contador in range(0,num,1):
    idade = int(input("Informe a sua idade: "))

    if(contador==1):
        idade_maior = idade
        idade_menor = idade
    else:
        if(idade > idade_maior):
            idade_maior = idade
        else:
            if(idade < idade_menor):
                idade_menor = idade
    idade_soma += idade

    
idade_media = idade_soma / num


print(f"A idade media é: {idade_media}")
print(f"A maior idade é: {idade_maior}")
print(f"A menor idade é: {idade_menor}")