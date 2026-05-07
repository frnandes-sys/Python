import random

def perder():
    print("\n=== CASA DE APOSTAS ===")

    interval = int(input("\nDigite um número: "))

    if interval == 0:
        print("\nNúmero sorteado: 1")
        print("\nVocê perdeu")
    elif interval == 1:
        print("\nNúmero sorteado: 0")
        print("\nVocê perdeu")

    input("\nDeseja continuar? Aperte 'Enter'")
    while True:
        return aposta()

def aposta():
    print("\n=== CASA DE APOSTAS ===")

    interval = int(input("\nDigite um número: "))

    while interval not in (0,1):
       interval = int(input("Digite um número: "))

    input("\nAperte 'Enter' para continuar")

    numero = random.randint(0,1)

    if numero == interval:
        print(f"\nNúmero sorteado: {numero}")
        print(f"\nVocê ganhou!")
    else:
        print(f"\nNúmero sorteado: {numero}")
        print(f"\nVocê perdeu!")
    print()

    input("\nDeseja continuar? Aperte 'Enter'")
    while True:
        return perder()

aposta()