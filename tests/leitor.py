print("====  CONCESSIONÁRIA  ====")

print("1 - ESPORTIVO")
print("2 - SUVS")
print("3 - SEDANS")

choice = input("\nQual sua escolha: ")
print("\n" * 100)

if choice == '1':
    with open('sports/sport.txt', 'r') as archive:
        arquivos = archive.readlines()

elif choice == '2':
    with open('suv/suvs.txt', 'r') as archive:
        arquivos = archive.readlines()

elif choice == '3':
    with open ('sedan/sedans.txt', 'r') as archive:
        arquivos = archive.readlines()

for arquivo in arquivos:
    print(arquivo)