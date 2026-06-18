horas = float(input("Digite as horas"))

salario = horas * 40.50

if salario > 2500:
    excedente = salario - 2500
    imposto = excedente * 0.11
    salario_liq = salario - imposto

else:
    salario_liq = salario

print(f"O salario liquido é {salario_liq:.2f}")