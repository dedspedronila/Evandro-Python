contador_masc = 0
contador_fem = 0
idade_media = 0
idade = 0
soma_idade = 0
idade_maior = 0

for num in range(0,20,1):
    idade = int(input("Informe a sua idade: "))
    sexo = input("Informe o seu sexo, M para Masculino e F para feminino:").strip()


    if(idade >= 18):
        idade_maior += 1


    soma_idade += idade

    if sexo.upper() == "M":
        contador_masc += 1
    else:
        if sexo.upper() == "F":
            contador_fem += 1
        else:
            print("Código Inválido!")   


idade_media = soma_idade / 20

print("Desculpe, a turma está lotada!")
print(f"Foram inscritas {contador_fem} mulheres")
print(f"A idade média foi de {idade_media}")
print(f"Inscritos maiores de idade foram {idade_maior} pessoas")



