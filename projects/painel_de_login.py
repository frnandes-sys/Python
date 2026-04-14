from contas import nomeusers, ident, passw, cash

# ------------------------------------------- INICIO

def inicio():
    print("\n=== Central Bank ===")
    print("\n1 - Entrar")
    print("2 - Registrar")
    print("3 - Sair")

    resposta = input("\nEscolha uma opção: ")

    while resposta not in ["1", "2", "3"]:
        print("\nOpção inválida! Tente novamente!")
        resposta = input("\nEscolha uma opção: ")

    if resposta == "1":
        print("\n" * 100)
        log()
    elif resposta == "2":
        print("\n" * 100)
        register()
    elif resposta == "3":
        print("\n" * 100)
        print("Até a próxima!")
        print("Finalizando...")

# ------------------------------------------- DEPOSITO

def depositar(index):

    print("\n=== Depósito ===")

    try:
        valor = float(input("\nDigite o valor a ser depositado: "))

        while valor <= 0:
            print("\n❌ | O valor deve ser maior que 0")
            valor = float(input("\nDigite o valor a ser depositado: "))

    except ValueError:
        print("\n❌ | Digite apenas números")
        return depositar(index)

    cash[index] += valor
    print(f"\n✅ | Depósito de R$ {valor} realizado com sucesso!")
    banco(index)

# ------------------------------------------- TRANSFERENCIA

def transferir(index):

    print("\n=== Transferência ===")

    entrada = input("\nDigite a chave PIX: ")

    while len(entrada) != 11:
        print("\n❌ | A chave PIX deve conter 11 números")
        entrada = int(input("Digite a chave PIX: "))

    valor = float(input("\nDigite o valor a ser transferido: "))

    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
        valor = float(input("\nDigite o valor a ser transferido: "))

    if valor <= cash[index]:
        cash[index] -= valor
        print(f"\n✅ | Transferência de R$ {valor} realizada com sucesso!")
    else:
        print("\n" * 10)
        print("\n❌ | Saldo insuficiente")
        return transferir(index)

    banco(index)

# ------------------------------------------- SAQUE

def sacar(index):

    print("\n=== Saque ===")

    valor = float(input("\nDigite o valor do saque: "))

    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
        valor = float(input("\nDigite o valor do saque: "))

    if valor <= cash[index]:
        cash[index] -= valor
        print(f"\n✅ | Saque de R$ {valor} realizado com sucesso!")
    else:
        print("\n" * 10)
        print("\n❌ | Saldo insuficiente")
        return transferir()

    banco(index)

# ------------------------------------------- BANCO

def banco(index):

    print(f"\n=== Olá, {nomeusers[index]} ===")

    print(f"\nSaldo: R$ {cash[index]}")

    print("\n1 - Depositar")
    print("2 - Transferir")
    print("3 - Sacar")
    print("4 - Sair")

    bank = input("\nEscolha uma opção: ")

    if bank == "1":
        depositar(index)
    elif bank == "2":
        transferir(index)
    elif bank == "3":
        sacar(index)
    elif bank == "4":
        print("Saindo…!")
        exit()

# ------------------------------------------- LOGIN

def log():
    print("\n=== Login ===")
    print("\nInsira '0' para voltar")
    cpf = input("\nDigite seu CPF: ").strip()

    if cpf == "0":
        return inicio()

    while len(cpf) !=11:
        print("\n❌ |O CPF deve conter 11 números")
        cpf = input("\nDigite seu CPF: ").strip()

    while cpf not in ident:
        print("\n❌ | CPF não cadastrado")
        cpf = input("\nDigite seu CPF: ").strip()

    index = ident.index(cpf)
   
    senha = input("\nDigite a senha: ").strip()

    while senha not in passw:
        print("\n❌ | Senha incorreta! Tente novamente.")
        senha = input("\nDigite a senha: ").strip()

    if senha == passw[index]:

        print("✅ | \nConta acessada com sucesso!")
        print("\n" * 100)
        banco(index)

# ------------------------------------------- REGISTRO

def register():
    print("\n=== Cadastro ===")
    nome = input("\nDigite seu nome: ").strip()
    cpf = input("\nDigite seu CPF: ").strip()

    while len(cpf) !=11:
        print("\n❌ | CPF inválido, tente novamente!")
        cpf = input("\nDigite seu CPF: ").strip()

    senha = input("\nDigite a senha: ").strip()

    while len(senha) < 5:
        print("\n❌ | A senha deve conter mais de 5 dígitos!")
        senha = input("\nDigite a senha: ")

    senha2 = input("\nConfirme sua senha: ")

    while senha2 != senha:
        print("\n❌ | A senha não confere! Tente novamente")
        senha2 = input("Confirme sua senha: ")

    with open('contas.py', 'a') as arquivo:
            arquivo.write(f"""\nnomeusers = ["{nome}"]
ident = ["{cpf}"]
passw = ["{senha}"]
cash = []
""")

    #cash.append(0)

    print("\n✅ | Cadastro realizado com sucesso!")
    print("\n" * 8)
    log()


if __name__ == "__main__":
    inicio()