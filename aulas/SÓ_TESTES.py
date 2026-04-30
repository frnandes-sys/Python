entrada = input('Digite um frase: ')

contagem_caracteres = {}

for caractere in entrada:
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

for caractere, contagem in contagem_caracteres.items():
    print(f"{caractere} {contagem} ocorrências")