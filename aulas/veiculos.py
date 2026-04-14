class Veiculos:
    def __init__(self, marca, modelo, velocidade, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
        self.combustivel = combustivel

    def veh(self):
        return(f"Marca: {self.marca} \nModelo: {self.modelo} \nVelocidade: {self.velocidade} \nCombustível: {self.combustivel}")

marca = input("Digite a marca do veículo: ")

while not marca.isalpha():
    print("Digite apenas letras!")
    marca = input("Digite a marca do veículo: ")

modelo = input("Digite o modelo do veículo: ")

while True:
    velocidade = input("Digite a velocidade do veículo: ")
    try:
        velocidade = float(velocidade)
        break
    except ValueError:
        print("Digite apenas números!")

interval = input("Carro elétrico?")

if interval.lower() == 'sim':
    autonomia = input("Digite a autonomia: ")

while interval.lower() != "sim":
    combustivel = input("Digite o combustivel do veículo: ")
    try:
        combustivel = float(combustivel)
        break
    except ValueError:
        print("Digite apenas números!")

veiculo1 = Veiculos(marca, modelo, velocidade, combustivel)

print(veiculo1.veh())

if interval == 'sim':
    with open(f"veiculos/{modelo}.txt", 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"Marca: {marca} \nModelo: {modelo} \nElétrico: {interval} \nVelocidade: {velocidade}Km \nAutonomia: {autonomia}")

if interval != 'sim':
    with open(f"veiculos/{modelo}.txt", 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"Marca: {marca} \nModelo: {modelo} \nElétrico: {interval} \nVelocidade: {velocidade}Km \nCombustível: {combustivel}L")