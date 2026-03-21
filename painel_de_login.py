loggin = []
password = []
users = []
moneys = []

def inicio():
    print("=== Central Bank ===")
    print("\n1 - Entrar na conta")
    print("2 - Registrar")
    print("3 - Sair")
    resposta = input("\nEscolha uma opção: ")

    if resposta == "1":
        log()
    elif resposta == "2":
        register()
    elif resposta == "3":
        print("Até a próxima!")
        print("Finalizando...")

def depositar():
    print("=== Depósito ===")
    valor = float(input("\nDigite o valor a ser depositado: "))
    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
    moneys.insert(1, valor)
    print(f"\nDepósito de R$ {valor} realizado com sucesso!")
    banco()

def banco():
    for user in users:
        usuario = user
    print(f"=== Olá, {usuario} ===")
    
    for money in moneys:
        print(f"\nSaldo: R$ {money}")
    print()
    print("1 - Depositar")
    print("2 - Transferir")
    print("3 - Sacar")
    print("4 - Sair")
    bank = input("\nEscolha uma opção: ")
    if bank == "1":
        depositar()
    elif bank == "2":
        transferir()
    elif bank == "3":
        sacar()
    elif bank == "4":
        print("Até a próxima!")
        exit()

def log ():
    print("=== Login ===")
    cpf = input("\nDigite seu CPF: ").strip()
    if cpf == "0":
        return inicio()

    while len(cpf) !=11:
        print("\n❌ |O CPF deve conter 11 números")
        cpf = input("\nDigite seu CPF: ").strip()

    while cpf not in loggin:
        print("❌ | CPF não cadastrado")
        cpf = input("Digite seu CPF: ").strip()

    index = loggin.index(cpf)

    senha = input("Digite a senha: ").strip()

    while senha not in password:
        print("\n❌ | Senha incorreta! Tente novamente.")
        senha = input("\nDigite a senha: ").strip()

    if senha == password[index]:

        print("\n" * 100)
        banco()

def register():
    print("=== Cadastro ===")
    nome = input("\nDigite seu nome: ")
    cpf = input("\nDigite seu CPF: ").strip()

    while len(cpf) !=11:
        print("\n❌ | CPF inválido, tente novamente!")
        cpf = input("\nDigite seu CPF: ").strip()

    senha = input("\nDigite a senha: ").strip()

    while len(senha) !=5:
        print("\n❌ | A senha deve conter mais de 5 dígitos!")
        senha = input("\nDigite a senha: ").strip()

    senha2 = input("\nConfirme sua senha: ")

    while senha != senha2:
        print("\n❌ | A senha não confere! Tente novamente")
        senha2 = input("Confirme sua senha: ")

    users.append(nome)
    loggin.append(cpf)
    password.append(senha)

    print("\n✅ | Cadastro realizado com sucesso!")
    print("\n" * 8)
    log()

inicio()