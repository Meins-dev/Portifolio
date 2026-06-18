import os

def calcular_salario(horas_trabalhadas, valor_hora):
    salario_bruto = horas_trabalhadas * valor_hora
    return salario_bruto


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')