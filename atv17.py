altura = float(input("Digite sua altura \n"))
sexo = str(input("Digite seu genero \n"))

sexo = sexo.upper()


if sexo == "MASCULINO":
    calculo = (72.7 * altura)-58
    print(f"seu peso ideal é {calculo}")
elif sexo == "FEMININO":
    calculo = (62.1 * altura)-44.7
    print(f"seu peso ideal é {calculo}")

