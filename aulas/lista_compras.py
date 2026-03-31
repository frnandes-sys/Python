print("Bem vindo a lista de compras!")
print("Digite o nome do item que deseja colocar na lista ou 'sair' para encerrar:")

lista_compras = ["bota"]
item = input()

while item != "sair":
    lista_compras.append(item)
    item = input()

print("\nAqui está a sua lista de compras:")
for i, item in enumerate(lista_compras, start=1):
    print(f"{i}, {item}")