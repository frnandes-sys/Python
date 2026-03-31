try:
    numero = 6
adv = int(input("Adivinhe o número: "))

while adv != numero:
    print("Número incorreto, tente novamente!")
    adv = int(input("Adivinhe o número: "))
else:
    print("Parabéns, você acertou o número!")

except ValueError:
print("Este numero não é inteiro.")
