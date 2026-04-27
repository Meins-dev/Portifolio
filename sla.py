def converter_dolar(valor_real, cotacao_dolar):
   return valor_real / cotacao_dolar



valor_real = float(input("Digite o valor da compra em reais : \n"))
cotacao_dolar = float(input("Digite a cotação do dolar: \n"))

resultado = converter_dolar(valor_real, cotacao_dolar)
print(f"O valor da compra em reais R$ {valor_real}, em dolar US${resultado:.2f}")