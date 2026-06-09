import sys
import os   

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def alunos():
    nome = []
    notas = []
    for i in range(4):
        nome.append(input(f"Digite o nome do aluno {i + 1}: "))
        notas.append(float(input(f"Digite a nota do aluno {i + 1}: ")))
    print("\n=== Alunos e Notas ===")
    for i in range(4):
        print(f"Aluno: {nome[i]}, Nota: {notas[i]:.2f}")

def sintuacao_escolar(notas, nome):
    media = 7
    for i in range(len(notas)):
        if notas[i] >= media:
            print(f"Aluno: {nome[i]} - Aprovado")
        elif notas[i] >= 6.9:
            print(f"Aluno: {nome[i]} - Recuperação")
        else:
            print(f"Aluno: {nome[i]} - Reprovado")
 

def listar_alunos(notas, nome):
    print("=== Lista de Alunos ===")
    for i in range(4):
        print(f"Aluno: {nome[i]}, Nota: {notas[i]:.2f}")
        nota_maxima = max(notas)
        if notas[i] == nota_maxima:
            print(f"Aluno com a maior nota: {nome[i]} - Nota: {notas[i]:.2f}")
            media_turma = sum(notas) / len(notas)
            print(f"Média da turma: {media_turma:.2f}")

def consultar_aluno(notas, nome):
    nome_consulta = input("Digite o nome do aluno para consulta: ")
    for i in range(4):
        if nome[i].lower() == nome_consulta.lower():
            print(f"Aluno: {nome[i]}, Nota: {notas[i]:.2f}")
            return
    print("Aluno não encontrado.")

def encerrar_programa():
    print("Encerrando o programa. Até mais!")
    sys.exit(0)

def main_menu(notas =[], nome = []):
    notas = []
    nome = []
    while True:
        print("=== Sistema Escolar ===")
        print("1. Cadastrar Alunos e Notas")
        print("2. Situação Escolar")
        print("3. Listar Alunos")
        print("4. Consultar Aluno")
        print("5. Encerrar Programa")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            alunos()
        elif escolha == '2':
            sintuacao_escolar(notas, nome)
        elif escolha == '3':
            listar_alunos(notas, nome)
        elif escolha == '4':
            consultar_aluno(notas, nome)
        elif escolha == '5':
            encerrar_programa()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()
    sys.exit(0)