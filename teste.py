peso = float(input("Digite seu peso \n"))
altura = float(input("Digite sua altura \n"))

imc = peso / (altura ** 2)



print("seu IMC é %.2f"%(imc))


nome = "alice" 
idade = 30
print("%s tem {} anos de idade e seu imc é de %.2f".format(idade) %(nome,imc))

destino1 = "Copa cabana"
destino2 = "barra da tijuca"
visitas = 2
print("Eu visitei hoje a {}, depois desçemos para {} , no total foram {} visitas".format(destino1,destino2,visitas))

nome2 = "Ederson" 
sobrenome = "Costa"

print("prezado {} {} Olá!".format(nome2,sobrenome))

print("+"+10*"-"+"+")
print(("|"+" "*10+"\n")*5,end="")
print("+"+10*"-"+"+")