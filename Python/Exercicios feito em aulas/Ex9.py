#Outra forma do EX8, com o retorno

def somar_numeros(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundonúmero: "))

somar_numeros(n1,n2)

print(f"O resultado da soma é {somar_numeros(n1,n2)}")