# meu_dicionario = {'chave1': 10, 'chave2': 20, 'chave3': 11}
# chaves = meu_dicionario.keys()
#
# print(chaves)
#
# meu_dicionario = {'chave1': 10, 'chave2': 20, 'chave3': 11}
# valores = meu_dicionario.values()
#
# print(valores)
#
# meu_dicionario = {'chave1': 10, 'chave2': 20, 'chave3': 11}
# pares_chave_valor = meu_dicionario.items()
#
# print(pares_chave_valor)

meu_dicionario = {'chave1': 10, 'chave2': 20, 'chave3': 30}

# valor_chave1 = meu_dicionario.get('chave1')
#
# print(valor_chave1)
#
# valor_chave4 = meu_dicionario.get('chave4', 40)
#
# print(valor_chave4)

outro_dicionario = {'chave2': 50, 'chave3': 60, 'chave4': 70}
meu_dicionario.update(outro_dicionario)
valores = meu_dicionario.values()

print(meu_dicionario)
print(valores)