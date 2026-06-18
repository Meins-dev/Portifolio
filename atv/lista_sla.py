lista = [0,1,2,3,4,5,6,7,8,9,10]

intervalo1 = lista[1:10]

intervalo2 = lista[8:11]

pares = []
for n in lista:
    if n % 2 == 0 : 
        if n == 0: 
            x = 0
    
        else:
            pares.append(n)


impares = []
for n in lista:
    if n % 2 != 0:
        impares.append(n)

reversa = lista[::-1]

soma = sum(lista)

tamanho = len(lista)

print(intervalo1,intervalo2,pares,impares,reversa,soma,tamanho)

