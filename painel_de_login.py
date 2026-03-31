loggin = []
password = []
users = []
moneys = []

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

def depositar(index):
    print("\n=== Depósito ===")
    valor = float(input("\nDigite o valor a ser depositado: "))

    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
        valor = float(input("\nDigite o valor novamente: "))

    moneys[index] += valor
    print(f"\nDepósito de R$ {valor} realizado com sucesso!")
    banco(index)

def transferir(index):
    print("\n=== Transferência ===")

    entrada = input("\nDigite a chave PIX: ")

    while len(entrada) != 11:
        print("\n❌ | A chave PIX deve conter 11 números")
        entrada = int(input("Digite a chave PIX: "))

    valor = float(input("\nDigite o valor a ser transferido: "))

    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
        valor = float(input("\nDigite novamente: "))

    if valor <= moneys[index]:
        moneys[index] -= valor
        print(f"\nTransferência de R$ {valor} realizada com sucesso!")
    else:
        print("\n❌ | Saldo insuficiente")

    banco(index)

def banco(index):
    #usuario = users[index]
  #  saldo = moneys[index]


    #print(f"\n=== Olá, {usuario} ===")

   # print(f"\nSaldo: R$ {saldo}")

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

def log():
    print("\n=== Login ===")
    print("\nInsira '0' para voltar")
    cpf = input("\nDigite seu CPF: ").strip()

    if cpf == "0":
        return inicio()

    #from contas import ident, password

    while len(cpf) !=11:
        print("\n❌ |O CPF deve conter 11 números")
        cpf = input("\nDigite seu CPF: ").strip()

    from contas import ident, passw

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
            arquivo.write(f"""\nusers = ["{nome}"]
ident = ["{cpf}"]
passw = ["{senha}"]
""")

    users.append(nome)
    loggin.append(cpf)
    password.append(senha)
    moneys.append(0)

    print("\n✅ | Cadastro realizado com sucesso!")
    print("\n" * 8)
    log()

inicio()