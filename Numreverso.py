def numero_reverso(n):
    reverso = 0
    while n > 0:
        digito = n % 10
        reverso = reverso * 10 + digito
        n //= 10
    return reverso

if __name__ == "__main__":
    numero = int(input("Digite um número inteiro: "))
    reverso = numero_reverso(numero)
    print(f"O número reverso de {numero} é {reverso}.")