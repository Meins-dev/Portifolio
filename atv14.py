nota1 = float(input("Digite a nota"))
nota2 = float(input("Digite a nota"))

if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
    print("nota invalida")
else:
    media = (nota1 + nota2) / 2 
    print(f"media é de {media:.2f}")