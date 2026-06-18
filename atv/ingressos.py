import os
import sys
from unittest import case, main

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def cadastro():
    nome = input("Digite o nome do cliente: ")
    limpar_tela()



def comprar_ingresso():
    quantidade = int(input("Digite a quantidade de ingressos: "))
    limpar_tela()
    if quantidade > 0:
        print(f"{quantidade} ingressos comprados com sucesso!")
    else:
        print("Quantidade inválida. Nenhum ingresso comprado.")
        sys.exit()

def valores_ingressos():
    print("=== Valores dos Ingressos ===")
    vip = 150.00
    camarote = 250.00
    pista = 50.00
    print(f"Valor do ingresso VIP: R$ {vip:.2f}")
    print(f"Valor do ingresso Camarote: R$ {camarote:.2f}")
    print(f"Valor do ingresso Pista: R$ {pista:.2f}")

def venda_ingresso():
    tipo_ingresso = input("Digite o tipo de ingresso (VIP, Camarote, Pista): ").strip().lower()
    if tipo_ingresso == "camarote":
        print("Ingresso Camarote vendido por R$ 250.00")
    elif tipo_ingresso == "vip":
        print("Ingresso VIP vendido por R$ 150.00")
    elif tipo_ingresso == "pista":
        print("Ingresso Pista vendido por R$ 50.00")
    else:
        print("Tipo de ingresso inválido. Nenhum ingresso vendido.")
        sys.exit()


def estoque_ingressos():
    print("=== Estoque de Ingressos ===")
    estoque_vip = 50
    estoque_camarote = 30
    estoque_pista = 100
    print(f"Estoque de ingressos VIP: {estoque_vip}")
    print(f"Estoque de ingressos Camarote: {estoque_camarote}")
    print(f"Estoque de ingressos Pista: {estoque_pista}")
    limpar_tela()


def main_menu():
    while True:
        print("=== Sistema de Ingressos ===")
        print("1. Cadastro do Cliente")
        print("2. Comprar Ingresso")
        print("3. Valores dos Ingressos")
        print("4. Resumo da Compra")
        print("5. Estoque de Ingressos")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        limpar_tela()
        match escolha:
                case '1':
                    cadastro()
                case '2':
                    comprar_ingresso()
                case '3':
                    valores_ingressos()
                case '4':
                    venda_ingresso()
                case '5':
                    estoque_ingressos()
                case '6':
                    print("Encerrando o sistema. Obrigado por usar nosso serviço!")
                case _:
                    print("Opção inválida. Tente novamente.")
                    continuar = input("Deseja continuar? (s/n): ")
                    if continuar.lower() != 's':
                        print("Encerrando o sistema. Obrigado por usar nosso serviço!")
                        break

main_menu()