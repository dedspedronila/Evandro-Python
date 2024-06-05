contador = 1
total = 0
soma_sal = 0
soma_filhos = 0
media_sal = 0.0
media_filhos = 0.0
sal_menor = 0
maior = 0
while contador != 0:
    salario = float(input("Informe o seu salário: "))
    filhos = int(input("Informe quantos filhos você tem: "))

    soma_sal += salario
    total += 1
    soma_filhos += filhos

    contador = int(input("Se deseja parar informe 0: "))

    if(salario <= 1000.00):
        sal_menor += 1


    if(salario > maior):
        maior = salario

media_sal = soma_sal / total
media_filhos = soma_filhos / total
media_sal_menor = (sal_menor / total) * 100
print(f"O maior salario é de: {maior}")
print(f"A media salarial é: {media_sal}")
print(f"A media do número de filhos é de: {media_filhos}")
print(f"A porcentagem de quem recebe até R$1000.00 é de: {media_sal_menor} %")
