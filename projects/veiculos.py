class Veiculos:
    def __init__(self, marca, modelo, ano, velocidade, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.combustivel = combustivel

    def veh(self):
        return(f"Marca: {self.marca} \nModelo: {self.modelo} \nAno? {self.ano} \nVelocidade: {self.velocidade} \nCombustível: {self.combustivel}")

marca = input("Digite a marca do veículo: ")

while not marca.isalpha():
    print("Digite apenas letras!")
    marca = input("Digite a marca do veículo: ")

modelo = input("Digite o modelo do veículo: ")

ano = input("Digite o ano do veículo: ")

while not ano.isdigit():
    print("Digite apenas números!")
    ano = input("Digite o ano do veículo: ")

while True:
    velocidade = input("Digite a velocidade do veículo: ")
    try:
        velocidade = float(velocidade)
        break
    except ValueError:
        print("Digite apenas números!")

while True:
    combustivel = input("Digite o combustivel do veículo: ")
    try:
        combustivel = float(combustivel)
        break
    except ValueError:
        print("Digite apenas números!")

veiculo1 = Veiculos(marca, modelo, ano, velocidade, combustivel)


print(veiculo1.veh())

with open(f"veiculos/{marca} {modelo}.txt", 'a', encoding='utf-8') as arquivo:
    arquivo.write(f"=== {marca} {modelo} === \n \nMarca: {marca} \nModelo: {modelo} \nAno: {ano} \nVelocidade: {velocidade}Km \nCombustível: {combustivel}L")