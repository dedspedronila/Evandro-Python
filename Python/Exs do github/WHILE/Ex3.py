alist ="S"
contador = 0
n_apto = 0
while alist != "N":
    nome= input("Informe seu nome: ")
    sexo= input("Informe seu sexo, M para masculino e F para feminino: ").strip()
    idade = int(input("Informe sua idade: "))
    saude = input("Informe sua saúde se boa B, se ruim R: ").strip()

    if(saude.upper() == "B") and (idade >=18) and (sexo.upper() == "M"):
        print(f"Conscrito {nome}, o senhor está aprovado!")
        contador +=1
    elif(saude.upper() == "R"):
            print(f"Conscrito {nome},o senhor está reprovado! Motivo: Sua saúde é ruim!")
            n_apto +=1
    elif(idade <18):
                print(f"Conscrito {nome},o senhor está reprovado! Motivo: Você é menor de idade!")
                n_apto +=1
    elif(sexo.upper() == "F"):
                    print(f"Conscrita {nome},a senhora está reprovado! Motivo: Mulheres estão dispensadas do serviço")
                    n_apto +=1

    alist = input("Para sair do cadastramento, informe a tecla N ").strip()


if alist.upper() == "N":
    print(f"{contador} foram aptos no cadastramento e {n_apto} não foram aprovados no cadastramento!")

