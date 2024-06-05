porc_canal_9 = 0
porc_canal_12 = 0
porc_canal_23 = 0
porc_canal_40 = 0
porc_canal_outros = 0
pessoas_canal = 0
cont_canal_9 = 0
cont_canal_12 = 0
cont_canal_23 = 0
cont_canal_40 = 0
cont_canal_outros = 0

canal = 1
while canal !=0:
    canal = int(input("Informe o seu canal preferido, o canal 9, 12, 23, 40 ou outros |Informe 0 para encerrar: "))
    
    if(canal == 9):
        cont_canal_9 +=1
        pessoas_canal += 1
    else:
        if(canal == 12):
            cont_canal_12 +=1
            pessoas_canal += 1
        else:
            if(canal == 23):
                cont_canal_23 +=1
                pessoas_canal += 1
            else:
                if(canal == 40):
                    cont_canal_40 +=1
                    pessoas_canal += 1
                else:
                    if(canal !=0):
                        cont_canal_outros +=1
                        pessoas_canal += 1
                    

if(pessoas_canal != 0):
    porc_canal_9 = (cont_canal_9 / pessoas_canal) *100
    porc_canal_12 = (cont_canal_12 / pessoas_canal) *100
    porc_canal_23 = (cont_canal_23 / pessoas_canal) *100
    porc_canal_40 = (cont_canal_40  / pessoas_canal) *100
    porc_canal_outros = (cont_canal_outros / pessoas_canal) *100

print(f"Porcentagem de telespectadores do canal 9 é de: {porc_canal_9:,.2f}")
print(f"Porcentagem de telespectadores do canal 12 é de: {porc_canal_12:,.2f}")
print(f"Porcentagem de telespectadores do canal 23 é de: {porc_canal_23:,.2f}")
print(f"Porcentagem de telespectadores do canal 40 é de: {porc_canal_40:,.2f}")
print(f"Porcentagem de telespectadores dos outros canais é de: {porc_canal_outros:,.2f}")