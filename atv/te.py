
from random import shuffle

def embaralhar_palavra(palavra):
    letras = list(palavra)
    shuffle(letras)
    return ''.join(letras)

palavra = ""  # palavra fixa que queremos atingir
tentativas = 0

while True:
    embaralhada = embaralhar_palavra(palavra)
    tentativas += 1
    print(embaralhada)

    if embaralhada == "":
        print(f"\nConseguiu após {tentativas} tentativas!")
        break
