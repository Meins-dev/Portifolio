import sys
import os

def alunos():
    nome = []
    notas = []
    for i in range(4):
        nome.append(input(f"Digite o nome do aluno {i + 1}: "))
        notas.append(float(input(f"Digite a nota do aluno {i + 1}: ")))
    return nome, notas

def sintuacao_escolar(notas, nome):
    for i in range(len(notas)):
        if notas[i] >= 7:
            print(f"{nome[i]} - Aprovado")
        elif notas[i] >= 6.9:
            print(f"{nome[i]} - Recuperação")
        else:
            print(f"{nome[i]} - Reprovado")

def listar_alunos(notas, nome):
    nota_maxima = max(notas)
    media = sum(notas) / len(notas)
    
    for i in range(len(notas)):
        print(f"{nome[i]} - {notas[i]}")
        if notas[i] == nota_maxima:
            print(f"Maior nota: {nome[i]}")
    
    print(f"Média da turma: {media:.2f}")

def consultar_aluno(notas, nome):
    busca = input("Nome do aluno: ")
    for i in range(len(notas)):
        if nome[i].lower() == busca.lower():
            print(f"{nome[i]} - {notas[i]}")
            return
    print("Aluno não encontrado")

def main_menu():
    nome = []
    notas = []

    while True:
        print("\n1 - Cadastrar")
        print("2 - Situação")
        print("3 - Listar")
        print("4 - Consultar")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == '1':
            nome, notas = alunos()
        elif op == '2':
            sintuacao_escolar(notas, nome)
        elif op == '3':
            listar_alunos(notas, nome)
        elif op == '4':
            consultar_aluno(notas, nome)
        elif op == '5':
            sys.exit()
        else:
            print("Opção inválida")

main_menu()