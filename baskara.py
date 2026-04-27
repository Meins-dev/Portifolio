a = int(input("Digite o A"))
if a != 0:
    b = int(input("Digite o B"))
    c = int(input("Digite o C"))
    delta = (b**2 - (4 * a * c))
    if delta < 0:
        print(f"A equação possui uma raiz real")
    elif delta == 0: 
        raiz = -b / (2*a)
        print(f'a equação possui uma raiz real {raiz}')
        
    else: 
        raiz1 = (((-b +(delta**0.5))/ (2*a)))
        raiz2 = (((-b -(delta**0.5 ))/ (2*a)))
        print(f"A equação possui as raizes {raiz1:.2f} sendo a raiz positiva \nE a raiz negativa sendo {raiz2:.2f}")














else:
    print("equação não é de segundo grau")