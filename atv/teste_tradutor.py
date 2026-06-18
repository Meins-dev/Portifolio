import deep_translator

texto = input("Digite uma palavra ou frase: ")

traducao = deep_translator.GoogleTranslator(
    source='pt',
    target='en, es, fr, de, it, ja, zh-CN, ru, ar, hi'
).translate(texto)

print("Tradução:", traducao)