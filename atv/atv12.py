n1 = float(input("Digite o primeiro numero"))
n2 = float(input("Digite o segundo numero"))
maior = n1 > n2 or n2 > n1
if n1 > n2:
    dif = n1 - n2
    print(f"maior numero é o {n1}  e a diferença entre eles é {dif}")

elif n2 > n1: 
    dif = n2 - n1
    print(f"maior numero é o {n2}  ea diferença entre eles é {dif}")

else: 
    print(f"os numeros são iguais")
