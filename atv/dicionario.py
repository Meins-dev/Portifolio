agenda = {}

def cadastrar():
    while True:
        cpf = input("CPF: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")

        agenda[cpf] = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        }

        continuar = input("Deseja cadastrar outro? (s/n): ")

        if continuar.lower() == "n":
            break

        agenda[cpf] = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

  


def listar_agenda():
    print("\nAgenda:")
    for cpf, dados in agenda.items():
        print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")


  

print("\nAgenda:")

for cpf, dados in agenda.items():
    print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")

def pesquisar_cpf():
    encontrado = []
    busca = input("Digite o CPF para pesquisar: ")
    for cpf, dados in agenda.items():
        if cpf.startswith(busca):
            encontrado.append((cpf, dados))

    if encontrado:
        for cpf, dados in encontrado:
            print(f"CPF: {cpf}, Nome: {dados['nome']}, Idade: {dados['idade']}, Telefone: {dados['telefone']}")
    else:
        print("CPF não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Cadastrar")
        print("2 - Listar Agenda")
        print("3 - Pesquisar por CPF")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            listar_agenda()
        elif escolha == "3":
            pesquisar_cpf()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()