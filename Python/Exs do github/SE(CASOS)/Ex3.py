agua = int(input("Informe a quantidade de água que foi encontrada no solo: "))

if (agua <= 10):
    print("O solo é rochoso!")
else:
    if (agua >10) and (agua <= 40):
        print("O solo é firme!")
    else:
        if (agua >40) and (agua <=80):
            print("O solo é Pantanoso!")
        else:
            if (agua >80):
                print("A quantidade é inválida!")
