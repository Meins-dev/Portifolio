def soma_imposto(preco, taxa_imposto):
    valor_imposto = preco * (taxa_imposto / 100)
    preco_com_imposto = preco + valor_imposto
    return preco_com_imposto

def ler_preco_e_taxa():
    while True:
        try:
            preco = float(input("Digite o preço do item: "))
            taxa_imposto = float(input("Digite a taxa de imposto (em %): "))
            return preco, taxa_imposto
        except ValueError:
            print("Por favor, digite um valor numérico válido para o preço e a taxa de imposto.")

def calcular_preco_com_imposto():
    preco, taxa_imposto = ler_preco_e_taxa()
    preco_final = soma_imposto(preco, taxa_imposto)
    print(f"O preço do item com imposto é: {preco_final:.2f}")

calcular_preco_com_imposto()