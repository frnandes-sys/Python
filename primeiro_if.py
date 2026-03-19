limite_passageiros = 5
total_passageiros = int(input("Digite o numero de passageiros: "))

if  total_passageiros <= limite_passageiros:
    print("Valor nao excedido, boa viagem!")
else:
    print("Limite de passageiro foi excedido, não foi possivel continuar")