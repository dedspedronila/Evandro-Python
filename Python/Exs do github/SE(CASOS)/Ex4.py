nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
categoria = ""
if(idade >= 5) and (idade <=7):
    categoria = "Infantil A"
else:
    if(idade >= 8) and (idade <= 11):
        categoria = "Infantil B"
    else:
        if(idade >= 12) and (idade <= 13):
            categoria = "Juvenil A"
        else:
            if(idade >= 14) and (idade <= 17):
                categoria = "Juvenil B"
            else:
                if(idade >=18):
                    categoria = "Adulto"
                else:
                    categoria = "Este nadador não possui uma categoria válida!"

print(f"Nadador {nome}, voce possui {idade} anos e sua categoria é {categoria}")