def valorPagamento():
    diario = [] # quando não há tamanho definido, estamos criando uma lista ao invés de vetor


    while True:
        val = float(input("Informe o valor da prestação: "))
        dias = int(input("Informe quantos dias de atraso: "))
        if dias > 0:
            multa = 0.03
            multa_dia = 0.0001 * dias
            total = float(val+(val*multa_dia)+(val*multa))
        else:
            total= val

        print(f"O valor a ser pago é R${total}.")
        diario.append(total)  # Adiciona na lista o valor pago para depois imprimi-lo
        
        continuar = input("Continuar? S/N: ").upper()
        if continuar == 'N':
            break

    print(f"As prestações pagas de hoje foram {diario}")
    print(f"Encerrado")

valorPagamento()