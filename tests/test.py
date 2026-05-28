def adicionar_receita(valor, receita, categoria):
    receita.append(valor)
    print(f"O valor de {:.2f} foi adicionado na receita!").format(valor)
    categoria = input("Digite a categoria:")

    print(f"O valor de {valor:.2f} foi adicionado na receita")



def main():
    receita = []
    despesa = []
    valor = []
    categoria = []

    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == 1:
        valor = input("Digite o valor da receita: ")
        adicionar_receita(valor, receita, categoria)
