
def soma_cumulativa(lista):
    lista = [1,2,3]
    resultado = []
    total = 0
    for numero in lista:
        total += numero 
        resultado.append(total)
    return resultado
t = [1,2,3]
print(soma_cumulativa(t))
