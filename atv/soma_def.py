def soma(a, b, c ):
    return a + b + c

while True:
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = int(input("Digite o terceiro número: "))
        resultado = soma(a, b, c)
        print(f"A soma dos números é: {resultado}")
        break
    except ValueError:
        print("Por favor, digite apenas números inteiros.")