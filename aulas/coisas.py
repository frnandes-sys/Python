class Pessoa:
    def __init__(self, nome, idade, gosto):
        self.nome = nome
        self.gosto = gosto
        self. idade = idade

    def saudacao(self):
         return f"\nHi, my name is {self.nome}, i have {self.idade} years, and i like {self.gosto}."


nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
gosto = input("Digite algo que gosta: ")

pessoa1 = Pessoa(nome, idade, gosto)

print(pessoa1.saudacao())

with open('save.py', 'a') as arquivo:
    arquivo.write(f"\nHi, my name is {nome}, i have {idade} years, and i like {gosto}.")
