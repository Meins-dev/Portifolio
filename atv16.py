salario = float(input("Digite o salario"))
prest = float(input("digite o valor da pretação"))
limite = salario * 0.2

if prest > limite:
    print(f"emprestimo negado fiot")

else:
    print("emprestimo autorizado fiot")