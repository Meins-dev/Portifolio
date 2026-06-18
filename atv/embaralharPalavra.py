def embaralhar_palavra(palavra):
    from random import shuffle
    letras = list(palavra)
    shuffle(letras)
    return ''.join(letras)

palavra = input("Digite uma palavra: ")
palavra_embaralhada = embaralhar_palavra(palavra)
print(f"A palavra embaralhada é: {palavra_embaralhada}")


    