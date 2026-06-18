import os 
import sys
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_destino(destinos):
    limpar_tela()
    print("=== Cadastro de Destino ===")
    nome = input("Nome do destino: ").strip()
    if nome in destinos:
        print("Destino já cadastrado.")
        return
    preco = float(input("Preço do destino: R$ ").strip())
    destinos[nome] = preco
    print(f"Destino '{nome}' cadastrado com preço R$ {preco:.2f}.")

    quantidade = int(input("Quantidade de passagens: ").strip())
    if quantidade > 0:
        print(f"{quantidade} passagens para '{nome}' adicionadas ao estoque.")
    else:
        print("Quantidade inválida. Passagens não adicionadas.")

def listar_destinos(destinos):
    limpar_tela()
    print("=== Destinos Disponíveis ===")
    if not destinos:
        print("Nenhum destino cadastrado.")
        return
    for nome, preco in destinos.items():
        print(f"{nome}: R$ {preco:.2f}")

def vagas_restantes(destinos, vendas):
    limpar_tela()
    print("=== Vagas Restantes ===")
    for nome, preco in destinos.items():
        vendidos = vendas.get(nome, 0)
        print(f"{nome}: {vendidos} passagens vendidas")
    passagens_vendidas = sum(vendas.values())
    print(f"Total de passagens vendidas: {passagens_vendidas}")
    print(f"Total de passagens disponíveis: {sum(destinos.values()) - passagens_vendidas}")
    destino_mais_vendido = max(vendas, key=vendas.get) if vendas else "Nenhum destino vendido"
    print(f"Destino mais vendido: {destino_mais_vendido}")

def comprar_passagem(destinos, vendas):
    limpar_tela()
    print("=== Comprar Passagem ===")
    nome = input("Nome do destino: ").strip()
    if nome not in destinos:
        print("Destino não encontrado.")
        return
    preco = destinos[nome]
    vendas[nome] = vendas.get(nome, 0) + 1
    print(f"Passagem para '{nome}' comprada por R$ {preco:.2f}.")


def encerrar_sistema():
    limpar_tela()
    print("Encerrando o sistema. Obrigado por usar a Agência de Viagens!")
    exit()

def menu():
    print("\nEscolha uma opção:")
    print("1 - Cadastrar destino")
    print("2 - Listar destinos")
    print("3 - Vagas restantes")
    print("4 - Comprar passagem")
    print("5 - Encerrar sistema")
    print("6 - Valor total das vendas")

def main():
    destinos = {}
    vendas = {}

    while True:
        menu()
        opcao = input("Opção: ").strip()
        if opcao == '1':
            cadastrar_destino(destinos)
        elif opcao == '2':
            listar_destinos(destinos)
        elif opcao == '3':
            vagas_restantes(destinos, vendas)
        elif opcao == '4':
            comprar_passagem(destinos, vendas)
        elif opcao == '5':
            encerrar_sistema()
        elif opcao == '6':
            total_vendas = valor_total_vendas(destinos, vendas)
            print(f"Valor total das vendas: R$ {total_vendas:.2f}")
        else:
            print("Opção inválida. Escolha uma opção entre 1 e 6.")


def valor_total_vendas(destinos, vendas):
    total = 0
    for nome, quantidade in vendas.items():
        preco = destinos.get(nome, 0)
        total += preco * quantidade
    return total

if __name__ == "__main__":
    main()
    sys.exit(0) 

