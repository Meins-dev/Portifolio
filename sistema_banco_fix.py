clientes = []

def cadastrar():
    cliente = {
        "nome": input("Nome: "),
        "endereco": input("Endereço: "),
        "telefone": input("Telefone: "),
        "cpf": input("CPF: "),
        "agencia": input("Agência: "),
        "numero_conta": input("Número da conta: "),
        "email": input("E-mail: "),
        "data_nascimento": input("Data de nascimento: "),
        "tipo_conta": input("Tipo de conta: "),
        "senha": input("Senha: "),
        "limite_credito": float(input("Limite de crédito: ")),
        "saldo": 0.0
    }

    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!\n")

def listar():
    if len(clientes) == 0:
        print("\nNenhum cliente cadastrado.\n")
        return

    for i, c in enumerate(clientes):
        print(f"\n===== CLIENTE {i} =====")
        print(f"Nome: {c['nome']}")
        print(f"Endereço: {c['endereco']}")
        print(f"Telefone: {c['telefone']}")
        print(f"CPF: {c['cpf']}")
        print(f"Agência: {c['agencia']}")
        print(f"Número da Conta: {c['numero_conta']}")
        print(f"E-mail: {c['email']}")
        print(f"Data de Nascimento: {c['data_nascimento']}")
        print(f"Tipo de Conta: {c['tipo_conta']}")
        print(f"Senha: {c['senha']}")
        print(f"Limite de Crédito: {c['limite_credito']}")
        print(f"Saldo: {c['saldo']}")

def editar():
    listar()

    if len(clientes) == 0:
        return

    try:
        indice = int(input("\nDigite o índice do cliente: "))
        cliente = clientes[indice]

        print("\nSelecione o dado que deseja alterar:")
        print("1 - Nome")
        print("2 - Endereço")
        print("3 - Telefone")
        print("4 - CPF")
        print("5 - Agência")
        print("6 - Número da conta")
        print("7 - E-mail")
        print("8 - Data de nascimento")
        print("9 - Tipo de conta")
        print("10 - Senha")
        print("11 - Limite de crédito")

        opcao = input("Opção: ")

        if opcao == "1":
            cliente["nome"] = input("Novo nome: ")

        elif opcao == "2":
            cliente["endereco"] = input("Novo endereço: ")

        elif opcao == "3":
            cliente["telefone"] = input("Novo telefone: ")

        elif opcao == "4":
            cliente["cpf"] = input("Novo CPF: ")

        elif opcao == "5":
            cliente["agencia"] = input("Nova agência: ")

        elif opcao == "6":
            cliente["numero_conta"] = input("Novo número da conta: ")

        elif opcao == "7":
            cliente["email"] = input("Novo e-mail: ")

        elif opcao == "8":
            cliente["data_nascimento"] = input("Nova data de nascimento: ")

        elif opcao == "9":
            cliente["tipo_conta"] = input("Novo tipo de conta: ")

        elif opcao == "10":
            cliente["senha"] = input("Nova senha: ")

        elif opcao == "11":
            cliente["limite_credito"] = float(input("Novo limite: "))

        else:
            print("Opção inválida.")
            return

        print("\nDados atualizados com sucesso!\n")

    except:
        print("\nErro ao editar cliente.\n")

def excluir():
    listar()

    if len(clientes) == 0:
        return

    try:
        indice = int(input("\nDigite o índice do cliente para excluir: "))
        clientes.pop(indice)

        print("Cliente removido com sucesso!\n")

    except:
        print("Erro ao excluir cliente.\n")

def deposito():
    listar()

    if len(clientes) == 0:
        return

    try:
        indice = int(input("\nDigite o índice do cliente: "))
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            clientes[indice]["saldo"] += valor
            print("Depósito realizado!\n")
        else:
            print("Valor inválido.\n")

    except:
        print("Erro no depósito.\n")

def saque():
    listar()

    if len(clientes) == 0:
        return

    try:
        indice = int(input("\nDigite o índice do cliente: "))
        valor = float(input("Valor do saque: "))

        saldo = clientes[indice]["saldo"]
        limite = clientes[indice]["limite_credito"]

        if valor <= (saldo + limite):
            clientes[indice]["saldo"] -= valor
            print("Saque realizado!\n")
        else:
            print("Saldo + limite insuficiente.\n")

    except:
        print("Erro no saque.\n")

def menu():
    while True:

        print("===== SISTEMA BANCÁRIO =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Editar cliente")
        print("4 - Excluir cliente")
        print("5 - Depositar")
        print("6 - Sacar")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            editar()

        elif opcao == "4":
            excluir()

        elif opcao == "5":
            deposito()

        elif opcao == "6":
            saque()

        elif opcao == "7":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.\n")

menu()