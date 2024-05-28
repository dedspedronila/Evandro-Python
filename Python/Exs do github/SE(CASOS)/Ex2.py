tc = input("Tipo de Carro | G para Gasolina e A para Álcool: ").strip()

ct = int(input("Informe a capacidade do tanque em litros: "))

if tc.upper() == "A":
    print("O tipo do carro que foi escolhido é Álcool")
else:
    if tc.upper() == "G":
        print("O tipo de carro que foi escolhido é Gasolina")

preco = float(input("Informe o preço do combustível que condiz com o tipo do carro: "))
valor = ct * preco
print(f"O preço a ser pago para encher o tanque de combustível é de: R$ {valor:,.2f}")