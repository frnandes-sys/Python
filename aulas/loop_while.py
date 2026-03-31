numero = 47
tentativa = None
while tentativa != numero:
    tentativa = int(input("Adivinhe o número secreto: "))
    if tentativa != numero:
        print("Tente novamente!")
print("Parabéns, você acertou o número secreto!")
