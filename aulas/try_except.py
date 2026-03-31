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

# --------------------------------------------------- Except divisao por 0

try:
    numero = 10 / 0
    print(numero)

except ZeroDivisionError:
    print("O calculo nao pode ser divisivel por 0")

# ------------------------------------------------------ Except TypeError

try:
    numero = "10" + 3
    print(numero)

except TypeError:
    print("Erro, não pode ser calculado com uma string")

finally:
    print("Fim do programa!")