lista = [1,2,3,3,3,3,3,4,5,100,150,30]  

def media(lista):
    sum = 0
    for i in range(0,len(lista)):
        sum += lista[i]
    return sum/len(lista)

def near(lista, media):
    distancia = max(lista)  # pega o maior valor da lista
    print(f"Valor max: {distancia}")
    for idx in range(len(lista)):
        if abs(lista[idx]- media) < distancia:
            valor = lista[idx]
            distancia = abs(lista[idx] -media) #abs(pega o valor absoluto, ou seja, o módulo)
    return valor    

print(f"Valor da média: {media(lista)}")
print(f"Valor mais proximo a média: {near(lista, media(lista))}")