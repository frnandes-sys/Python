import painel_de_login
import contas


#print(painel_de_login.inicio())



digite = input("Digite um nome: ")
contas.nomeusers.append(digite)

for nomeuser in contas.nomeusers:
    print(nomeuser)


