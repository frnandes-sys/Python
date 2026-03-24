def calcular_ponderada(nota1, nota2, nota3, peso1, peso2, peso3):
    soma_pesos = peso1 + peso2 + peso3
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / soma_pesos
    return media_ponderada

entrada = input("Digite a primeira nota (ou 'sair'): ")

if entrada == "sair":
    print("Finalizado...")
    exit()

nota1 = float(entrada)
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso1 = float(input("Digite o primeiro peso: "))
peso2 = float(input("Digite o segundo peso: "))
peso3 = float(input("Digite o terceiro peso: "))

print("\nA média ponderada é:", calcular_ponderada(nota1, nota2, nota3, peso1, peso2, peso3))