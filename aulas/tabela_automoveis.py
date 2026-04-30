print("=== Tabela Media de Preços de Automoveis ===")

precos_carros = {}

precos_carros['HB20'] = [81722, 82478, 95790]
precos_carros['Ford KA'] = [34500, 38900, 42700]
precos_carros['Chevrolet Corsa'] = [20300, 24500, 32900]

media_carros = {}

for carros, precos in precos_carros.items():
    media = sum(precos) / len(precos)
    media_carros[carros] = media

for carros, media in media_carros.items():
    print(f"\nModelo: {carros} \nMédia de preço: {media:,.2f}".replace(',', 'X').replace('.',',').replace('X', '.'))
