class Car:
    def __init__(self, marca, model, ano):
        self.marca = marca
        self.model = model
        self.ano = ano

    def infos(self):
        return f"Marca: {self.marca}, Modelo: {self.model}, Ano: {self.ano}"

    def ano_antigo(self):
        return self.ano < 2000

veh1 = Car("Honda", "Civic", "2020")

veh2 = Car("Porshe", "Carrera", "2022")

veh3 = Car("Fiat", "Uno", "1984")

print("=== Concessionaria ===")
print()
print(veh1.infos())
print(veh1.ano_antigo())
print()
print(veh2.infos())
print(veh2.ano_antigo())
print()
print(veh3.infos())
print(veh3.ano_antigo())