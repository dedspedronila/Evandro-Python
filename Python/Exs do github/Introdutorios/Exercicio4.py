#Algoritmo
tempo = float(input("Informe o tempo gasto em horas:"))
km_litro = float(input("Informe a autonomia(KM/L) do carro:"))
velocidade = float(input("Informe a velocidade média em KM:"))

distancia = velocidade * tempo
velocidade_media = distancia / tempo
litros_totais = distancia / km_litro

print(f"A velocidade média foi: {velocidade_media}")
print(f"o tempo gasto foi de: {tempo}")
print(f"A distância percorrida foi de: {distancia}")
print(f"A quantidade de litros usados: {litros_totais} ")
