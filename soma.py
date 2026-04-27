km = float(input("Digite qnts km: "))
consumo = float(input("consumo do carro: "))
gasosa = float(input("Digite preço do combstivel: "))

litros = km / consumo
precomb = litros * gasosa
print(f"ai isso ai precisa de {litros:.2f} litros de gasosa. \nQue custara basicamente R$ {precomb:.2f} ")
