h = float(input("digite o numero do primeiro lado: "))
b = float(input("digite o numero do segundo lado: "))
a = float(input("digite o numero do terceiro lado: "))

if h + b > a or a + h > b or b + a > h:
    if h == b and b == a:
        print("equilatero")

    elif h == b or a == b or h == a:
        print("isocelis")

    else:
        print("escaleno")

else:
    print("não é um triangulo")

