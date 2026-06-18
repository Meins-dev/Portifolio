print("Bem vindo a calculadora 2000 - faz calculos sozinha")
while True:
    print("Menu da calculadora 2000 - \n1 - Soma \n2 - Multiplica \n3 - Divide, \n4 - subtração \n0-sair da calculadora 2000")
    dgt_tela = int(input("Digite o numero do menu que quer acessar: "))
    if dgt_tela == 1 : 
            print("Soma Selecionado")
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            total = x + y
            resultado = print(f"O resultado dessa soma é {total:.2f} \n")
    elif dgt_tela == 2:
            print("Multiplicação selecionado")
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            total = x * y
            resultado = print(f"O resultado dessa multiplicação é {total:.2f} \n")
    elif dgt_tela == 3 :
            print("Divisão selecionado")
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            total = x / y
            resultado = print(f"O resultado dessa divisão é {total:.2f} \n")
    elif dgt_tela == 4 :
            print("Subtração selecionado")
            x = float(input("Digite o primeiro numero: "))
            y = float(input("Digite o segundo numero: "))
            total = x - y
            resultado = print(f"O resultado dessa subtração é {total:.2f} \n")
    elif dgt_tela == 0 :
           break
    else:
           print("\nDigite uma opção valida \n")