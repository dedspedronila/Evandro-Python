#Variaveis(Não necessária)
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

#Algoritmo
nome = input("Informe o NOME do aluno: ")
nota1 = float(input("Informe a nota 1:"))
nota2 = float(input("Informe a nota 2:"))


media = (nota1 + nota2) / 2


#Parte nova com IF(2EXERCICIOS EM 1)
if(media >= 6):
    situacao = "Aprovado"
else:
    if(media >= 4) and (media <6):
            situacao = "Recuperação"
    else:
            situacao = "Reprovado"

print(f"{nome}, a sua média é: {media} e você está {situacao}")