def cadastro_peca():
    pc = {}
    pc['nome'] = input("Digite o nome da peça: ")
    pc['codigo'] = input("Digite o código da peça: ")
    pc['quantidade'] = int(input("Digite a quantidade da peça: "))
    pc['preco'] = float(input("Digite o preço da peça: "))
    return pc

def listar_pecas(pc):
    for p in pc:
        print(f"Nome: {p['nome']}, Código: {p['codigo']}, Quantidade: {p['quantidade']}, Preço: R${p['preco']:.2f}")


def venda_peca(pc):
    codigo = input("Digite o código da peça que deseja vender: ")
    for p in pc:
        if p['codigo'] == codigo:
            quantidade_venda = int(input("Digite a quantidade que deseja vender: "))
            if quantidade_venda <= p['quantidade']:
                p['quantidade'] -= quantidade_venda
                print(f"Venda realizada! Total: R${quantidade_venda * p['preco']:.2f}")
            else:
                print("Quantidade insuficiente em estoque.")
            return
    print("Peça não encontrada.")

def repor_estoque(pc):
    codigo = input("Digite o código da peça que deseja repor: ")
    for p in pc:
        if p['codigo'] == codigo:
            quantidade_reposicao = int(input("Digite a quantidade que deseja repor: "))
            p['quantidade'] += quantidade_reposicao
            print("Estoque atualizado.")
            return
    print("Peça não encontrada.")

def encerrar_programa():
    print("Encerrando o programa. Até mais!")
    exit()

def main_menu():
    pc = []
    while True:
        print("\n1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Vender peça")
        print("4 - Repor estoque")
        print("5 - Encerrar programa")

        op = input("Escolha: ")

        if op == '1':
            pc.append(cadastro_peca())
        elif op == '2':
            listar_pecas(pc)
        elif op == '3':
            venda_peca(pc)
        elif op == '4':
            repor_estoque(pc)
        elif op == '5':
            encerrar_programa()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()