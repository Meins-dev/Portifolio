salario = float(input("Digite o salario: "))
if salario < 500:
    novoSalario = salario + (salario*0.15)
elif salario >=500 and salario <= 1000:
    novoSalario = salario + (salario*0.1)
elif salario > 1000:
    novoSalario = salario + (salario*0.05)
print(f"O valor do salário reajustado será de R${novoSalario:.2f}") 
