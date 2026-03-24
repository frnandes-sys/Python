def somar(a, b):
    return a + b

while True:
    entrada = input("Digite o primeiro número (ou 'sair'): ")

    if entrada == "sair":
        print("Finalizando...")
        break

    primeiro = int(entrada)
    segundo = int(input("Digite outro numero: "))

    print("Valor total dos numeros digitados:", somar(primeiro, segundo))