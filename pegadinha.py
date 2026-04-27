n1 = float(input("Digite a nota 1 : "))
n2 = float(input("Digite a nota 2 : "))
media = (n1 + n2 ) / 2 
if media >= 7 and media < 10: 
    print(f"Aprovado")
elif media < 7:
    print("reprovado")
elif media == 10:
    print("Aprovado fiot 10 ")
