print("-- Resevartório de Água --")

altura =float (input(" Digite a altura (cm):"))
largura= float(input(" Digite a largura (cm): "))
comprimento=float(input(" Digite o comprimento (cm): "))
c_diario = float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=(altura * largura * comprimento) /1000
auton_reser = cap_total/c_diario

print(f"Capacidade do Reservatório= {cap_total} litros ")
print(f"Autonomia do reservatório= {auton_reser} dias \n Agora, vamos classificar o consumo")
if(auton_reser<2):
    print("Consumo Elevado")
elif auton_reser>=2 and auton_reser:
    print("Consumo Moderado")
elif(auton_reser>7):
    print("/n Consumo Baixo")
