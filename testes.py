print("Bem vindo a lista de compras!")
print("Digite um item para adicionar na sua lista de compras:")

lista_compras = []
item = input()

while item != "sair":
    lista_compras.append(item)
    item = input()

print("\nAqui está a sua lista de compras:") 
for i, item in enumerate(lista_compras, start=1):
    print(f"{i}, {item}")