import sys

def solicitar_nome():
    while True:
        nome = input("Informe o nome do cliente: ").strip()
        if nome:
            return nome
        print("Nome inválido. Digite um nome não vazio.")

def solicitar_valor_inicial():
    while True:
        try:
            valor = input("Saldo inicial (use '.' para decimais): ").strip()
            saldo = float(valor)
            if saldo < 0:
                print("Saldo inicial não pode ser negativo.")
                continue
            return saldo
        except ValueError:
            print("Entrada inválida. Digite um número válido para o saldo inicial.")

def solicitar_valor_positivo(prompt):
    while True:
        try:
            valor = input(prompt).strip()
            montante = float(valor)
            if montante <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return montante
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def depositar(conta, extrato, contadores):
    valor = solicitar_valor_positivo("Valor para depósito: ")
    conta['saldo'] += valor
    extrato.append(f"Depósito: +R$ {valor:.2f}")
    contadores['depositos'] += 1
    contadores['total_operacoes'] += 1
    print(f"Depósito realizado. Saldo atual: R$ {conta['saldo']:.2f}")

def sacar(conta, extrato, contadores):
    try:
        valor = solicitar_valor_positivo("Valor para saque: ")
    except KeyboardInterrupt:
        print()
        return
    if valor > conta['saldo']:
        print("Saque negado. Saldo insuficiente.")
        return
    conta['saldo'] -= valor
    extrato.append(f"Saque: -R$ {valor:.2f}")
    contadores['saques'] += 1
    contadores['total_operacoes'] += 1
    print(f"Saque realizado. Saldo atual: R$ {conta['saldo']:.2f}")

def consultar_saldo(conta, contadores):
    print(f"Saldo atual de {conta['nome']}: R$ {conta['saldo']:.2f}")
    contadores['consultas'] += 1
    contadores['total_operacoes'] += 1

def mostrar_extrato(extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for linha in extrato:
            print(linha)
    print("---------------\n")

def menu():
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Mostrar extrato")
    print("5 - Encerrar sistema")

def main():
    print("=== Cadastro de Conta ===")
    nome = solicitar_nome()
    saldo_inicial = solicitar_valor_inicial()
    conta = {'nome': nome, 'saldo': saldo_inicial}
    extrato = []
    contadores = {'depositos': 0, 'saques': 0, 'consultas': 0, 'total_operacoes': 0}

    print(f"\nConta criada para {conta['nome']} com saldo inicial R$ {conta['saldo']:.2f}")

    while True:
        menu()
        opcao = input("Opção: ").strip()
        if opcao == '1':
            depositar(conta, extrato, contadores)
        elif opcao == '2':
            sacar(conta, extrato, contadores)
        elif opcao == '3':
            consultar_saldo(conta, contadores)
        elif opcao == '4':
            mostrar_extrato(extrato)
        elif opcao == '5':
            print("\nEncerrando sistema...")
            print(f"Resumo para {conta['nome']}:")
            print(f"Saldo final: R$ {conta['saldo']:.2f}")
            print(f"Depósitos: {contadores['depositos']}, Saques: {contadores['saques']}, Consultas de saldo: {contadores['consultas']}")
            print(f"Total de operações: {contadores['total_operacoes']}")
            mostrar_extrato(extrato)
            break
        else:
            print("Opção inválida. Escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Encerrando.")
        sys.exit(0)

