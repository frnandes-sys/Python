loggin = ["12312312312"]
password = ["12345"]
users = ["Daniel"]
moneys = []

def inicio():
    print("\n=== Central Bank ===")
    print("\n1 - Entrar na conta")
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

def depositar():
    print("\n=== Depósito ===")
    valor = float(input("\nDigite o valor a ser depositado: "))
    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
    moneys.insert(1, valor)
    print(f"\nDepósito de R$ {valor} realizado com sucesso!")
    banco()

def transferir():
    print("\n=== Transferência ===")
    print("\nInsira '0' para voltar")
    print("\n1 - CPF")
    print("\n2 - Número de telefone")
    print("\n3 - E-mail")
    print("\n4 - Chave aleatória")

    transfer = input("\nEscolha uma opção: ")

    if transfer == "1":

        tcpf = input("\nDigite o CPF do destinatário: ")

        while len(tcpf) !=11:
            print("\n❌ | O CPF deve conter 11 números")
            tcpf = input("\nDigite o CPF do destinatário: ")

    valor = float(input("\nDigite o valor a ser transferido: "))
    
    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")

    if moneys >= valor:

        print(f"\nTransferência de R$ {valor} realizada com sucesso!")
        moneys.insert(1, (moneys - valor))
        banco()
    else:
        print("\n❌ | Saldo insuficiente")
        banco()

    if transfer == "2":
       num = input("\nDigite o número de telefone do destinatário: ")
       while len(num) !=11:
        print("\n❌ | O número de telefone deve conter 11 números")
        num = float(input("\nDigite o número de telefone do destinatário: "))
    valor = float(input("\nDigite o valor a ser transferido: "))
    while valor <= 0:
        print("\n❌ | O valor deve ser maior que 0")
        valor = float(input("\nDigite o valor a ser transferido:"))
        
        if valor <= money:
            print(f"\nTransferência de R$ {valor} realizada com sucesso!")
            moneys.insert(1, (moneys[1] - valor))
            banco()
        else:
            print("\n❌ | Saldo insuficiente")
            banco()

def banco():
    for user in users:
        usuario = user
    print(f"\n=== Olá, {usuario} ===")


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
        print("Saindo…!")
        exit()

def log ():
    print("\n=== Login ===")
    print("\nInsira '0' para voltar")
    cpf = input("\nDigite seu CPF: ").strip()
    if cpf == "0":
        return inicio()

    while len(cpf) !=11:
        print("\n❌ |O CPF deve conter 11 números")
        cpf = input("\nDigite seu CPF: ").strip()

    while cpf not in loggin:
        print("\n❌ | CPF não cadastrado")
        cpf = input("\nDigite seu CPF: ").strip()

    index = loggin.index(cpf)
   
    senha = input("\nDigite a senha: ").strip()

    while senha not in password:
        print("\n❌ | Senha incorreta! Tente novamente.")
        senha = input("\nDigite a senha: ").strip()

    if senha == password[index]:

        print("✅ | \nConta acessada com sucesso!")
        print("\n" * 100)
        banco()

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

    users.append(nome)
    loggin.append(cpf)
    password.append(senha)

    print("\n✅ | Cadastro realizado com sucesso!")
    print("\n" * 8)
    log()

inicio()