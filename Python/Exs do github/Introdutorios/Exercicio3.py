#Algoritmos
preco_fabrica = float(input("Informe o preço de fábrica do veículo:"))
percentual_lucro = float(input("Informe o percentual de lucro do distribuidor:"))
percentual_imposto = float(input("Informe o percentual de impostos:"))

percentual_imposto_calc = preco_fabrica * (percentual_imposto/100) 
percentual_imposto_final = preco_fabrica + percentual_imposto_calc

percentual_lucro_calc = percentual_imposto_final * (percentual_lucro/100)
percentual_lucro_final = percentual_imposto_final + percentual_imposto_calc

preco_consumidor = percentual_lucro_final + percentual_imposto_final


print (f"O valor correspondente aos impostos é de: {percentual_imposto_final}")
print (f"O valor correspondente ao lucro é de :{percentual_lucro_final}")
print (f"O valor final do veículo é de: {preco_consumidor}")
