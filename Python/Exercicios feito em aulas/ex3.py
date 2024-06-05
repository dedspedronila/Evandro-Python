numero = int(input("Informe o número para tabuada: "))
#For sempre o para obter o numero que você quer no fim, exemplo se quiser o numero 10 coloque 11 pois mostrará 11-1 = 10
for contador in range(1,11,1):
    print(f"{numero} X {contador} = {numero * contador}")