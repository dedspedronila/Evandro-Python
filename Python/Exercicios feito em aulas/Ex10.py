#função
def somar_numeros_3parametros(numero1, numero2):
    resultado = numero1 + numero2
    return numero1, numero2, resultado

n1, n2, resultado = somar_numeros_3parametros(3,5)

print(f"O 1º parametro foi {n1}")
print(f"O 2º parametro foi {n2}")
print(f"O resultado foi {resultado}")

