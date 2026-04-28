class Agenda:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def adicionar(self):
        return f"Nome: {self.name} | Número: {self.number}"

print("========== AGENDA DE CONTATOS ==========")
print()
pessoa1 = Agenda("Daniel", "71992126736")
pessoa2 = Agenda("Adriano", "71973645836")


print(pessoa1.adicionar())
print(pessoa2.adicionar())

