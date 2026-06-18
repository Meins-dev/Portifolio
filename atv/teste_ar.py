clientes = []

while True:
    print("\nCadastro de Clientes")

    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    cpf = input("Digite o cpf: ")

    # adiciona cliente na lista
    clientes.append({
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "cpf": cpf
    })

    print("\nClientes cadastrados:")
    for i, cliente in enumerate(clientes):
        print(f"{i} - {cliente['nome']}")

    opcao = input("\nDeseja excluir algum cliente? (s/n): ")

    if opcao == "s":
        if len(clientes) == 0:
            print("Não há clientes para excluir.")
        else:
            indice = int(input("Digite o número do cliente: "))

            if indice < 0 or indice >= len(clientes):
                print("Índice inválido!")
            else:
                cliente_removido = clientes.pop(indice)
                print(f"Cliente {cliente_removido['nome']} removido!")

    continuar = input("\nDeseja continuar? (s/n): ")
    if continuar != "s":
        break