loggin = []
password = []
users = []

def inicio():
    print("=== Central Bank ===")
    print()
    print("1 - Entrar na conta")
    print("2 - Registrar")
    print("3 - Sair")

def banco():
    for user in users:
        usuario = user
        #print(f"=== Central Bank - Olá {user}")
    print(f"=== Olá, {usuario} ===")
    print()
    print("1 - Depositar")
    print("2 - Transferir")
    print("3 - Sacar")
    print("4 - Sair")
    bank = input("\nEscolha uma opção: ")

def log ():
    cpf = input("Digite seu CPF: ").strip()

    while len(cpf) !=11:
        print("O CPF deve conter 11 números")
        cpf = input("Digite seu CPF: ").strip()


    while cpf not in loggin:
        print("CPF não cadastrado")
        cpf = input("Digite seu CPF: ").strip()

    index = loggin.index(cpf)

    senha = input("Digite a senha: ").strip()

    if senha == password[index]:

        print("\n" * 100)
        banco()
    else:
        print("Senha incorreta.")

def register():
    nome = input("Digite seu nome: ")
    cpf = input("\nDigite seu CPF: ").strip()

    while len(cpf) !=11:
        print("CPF inválido, tente novamente!")
        cpf = input("Digite seu CPF: ").strip()

    senha = input("Digite a senha: ").strip()

    while len(senha) !=5:
        print("A senha deve conter mais de 5 dígitos!")
        senha = input("Digite a senha: ").strip()

    senha2 = input("Confirme sua senha: ")

    while senha != senha2:
        print("A senha não confere! Tente novamente")
        senha2 = input("Confirme sua senha: ")

    users.append(nome)
    loggin.append(cpf)
    password.append(senha)

    print("\nCadastro realizado com sucesso!")
    print("\n" * 8)
    log()

inicio()
resposta = input("\nEscolha uma opção: ")

if resposta == "1":
    log()
elif resposta == "2":
    register()
elif resposta == "3":
    print("Finalizando...")