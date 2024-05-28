print("Vendas")
print("Produtos --- Pão Caseiro(Caseirinho) -> R$0,10| Broa de milho(Broinha) -> R$1,60")

produto1 = int(input("Informe quantos Pães Caseirinho deseja:"))
produto2 = int(input("Infrome quantas Broinhas desejas:"))

soma1 = produto1 * 0.1
soma2 = produto2 * 1.6

somatotal= soma1 + soma2 
poupanca = somatotal * 0.1

print(f"Foram vendidos {produto1} Caseirinhos, e {produto2} Broinhas, o total ganho foi de {somatotal} e o que deverá ser guardado é de {poupanca}")