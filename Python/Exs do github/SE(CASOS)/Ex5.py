salario = float(input("Informe o seu salário atual: "))

if(salario <= 500.00): 
    novosal = salario * 1.05
else:
    if(salario >500.00) and (salario <=1200.00):
        novosal = salario * 1.12
    else:
        if(salario > 1200.00):
            novosal = salario
        
aux = 0.0
if(salario <= 600.00):
    aux = novosal + 150.00
else:
    if(salario >=600.00):
        aux = novosal + 100.00

print(f"O valor do novo salário após as mudanças é de: R$ {aux:,.2f}")