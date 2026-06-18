print("Isso é um absurdo quero uma eleição -")
c1 = c2 = c3 = c4 = 0 
nulos = 0
branco = 0 
total = 0 
while True:
    print("Digite o numero do candidato equivalente ao que voce esta votando \n1 - zé felipe \n2 - Ferrugem \n3 - léo stronda \n4 - richard rasmut\n ")
    voto = input("Digite o numero do candidato que deseja voltar: ")
    if voto == "0":
        break
    if voto == "":
        branco += 1
        print("Voto computado para o voto em branco")
    else: 
        voto = int(voto)
        if voto == 1:
            c1 +=1
        elif voto == 2:
            c2 +=1
        elif voto == 3:
            c3 +=1 
        elif voto == 4:
            c4 +=1
        else:
            nulos += 1

    total += 1 

votos = [c1,c2,c3,c4]
ganhador = votos.index(max(votos)) + 1 

#resultados 

print(f"zé felipe {c1}")
print(f"Ferrugem {c2}")
print(f"léo stronda {c3}")
print(f"richard rasmut {c4}")
print(f"nulos {nulos}")
print(f"brancos {branco}")
print(f"Votos totais {total}")
print(f"Ganhador foi o candidato {ganhador}")
