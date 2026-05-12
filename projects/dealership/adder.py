adder = input('Digite qual carro deseja adicionar: ').upper()
value = float(input('Digite o valor do carro: '))

print("1 - ESPORTIVO \n2 - SUV \n3 - SEDAN")

which = input("Qual dessas opções indentifica o carro? ")

if which == "1":
    with open('sports/sport.txt', 'a', encoding='utf-8') as archive:
        archive.write(f"\n{adder} = {value:.3f},00")#.replace('.', ','))
        print("Carro adicionado com sucesso!")
        archive.close()

elif which == "2":
    with open('suv/suvs.txt', 'a', encoding='utf-8') as archive:
        archive.write(f"\n{adder} = {value:.3f},00")  # .replace('.', ','))
        print("Carro adicionado com sucesso!")
        archive.close()

elif which == "3":
    with open('sedan/sedans.txt', 'a', encoding='utf-8') as archive:
        archive.write(f"\n{adder} = {value:.3f},00")  # .replace('.', ','))
        print("Carro adicionado com sucesso!")
        archive.close()
