def valorPagamento(valorprestacao, diasAtraso):
    if diasAtraso == 0:
        return valorprestacao
    else:
        multa = valorprestacao * 0.03
        juros = valorprestacao * 0.001 * diasAtraso
        return valorprestacao + multa + juros

def relatorio_dia(dia, prestacoes):
    print(f"Relatório do dia {dia}:")
    for valor, atraso in prestacoes:
        valor = valorPagamento(valor, atraso)
        print(f"Valor da prestação: R${valor:.2f}, Dias de atraso: {atraso}, Valor a pagar: R${valor:.2f}")
    total = sum(valorPagamento(valor, atraso) for valor, atraso in prestacoes)
    print(f"Valor total a pagar no dia {dia}: R${total:.2f}")
    
if __name__ == "__main__":
    prestacoes = []
    while True:
        valor = float(input("Digite o valor da prestação (ou 0 para encerrar): "))
        if valor == 0:
            break
        atraso = int(input("Digite o número de dias de atraso: "))
        prestacoes.append((valor, atraso))

        dia = input("Digite o dia do relatório: ")
        relatorio_dia(dia, prestacoes)