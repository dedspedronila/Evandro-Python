print("Revendemos aqui sucos, temos nos formatos de : Lata de 350ML| Garrafa de 600ML| Garrafa de 2L")

item1 = int(input("Informe quantas latas de 350ML foram compradas:"))
item2 = int(input("Informe quantas garrafas de 600ML foram compradas:"))
item3 = int(input("Informe quantas garrafas de 2L foram compradas:"))

litros = (item1 * 0.35) + (item2 * 0.6) + (item3 * 2)
print(f"O total de litros comprados foi de : {litros}")
