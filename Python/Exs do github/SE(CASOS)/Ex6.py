salario_min = float(input("Informe o seu salário :"))
horas_trab = int(input("Informe quantas horas inteiras foram trabalhadas: "))
num_dependentes = int(input("Informe qual é o seu número de dependentes: "))
horas_extras = int(input("Informe a quantidade de horas extras trabalhadas: "))

horas_trab = 1/5 * salario_min
salario_mes = horas_trab * valor_hora
dependentes = 32 * num_dependentes
horas_extras_calc = horas_extras * 1.5
sal_bruto = salario_mes + dependentes + horas_extras_calc
