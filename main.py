import json

# -----------------------------
# salvar / carregar

def carregar_contas():
    try:
        with open("contas.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_contas(contas):
    with open("contas.json", "w") as arquivo:
        json.dump(contas, arquivo, indent=4)

# -----------------------------

def inicio():
    print("\n1 - Login")
    print("2 - Registrar")

    op = input("Escolha: ")

    if op == "1":
        log()
    elif op == "2":
        register()

# -----------------------------

def log():
    contas = carregar_contas()

    cpf = input("CPF: ")

    usuario = None

    for c in contas:
        if c["cpf"] == cpf:
            usuario = c
            break

    if usuario is None:
        print("CPF não encontrado")
        return

    senha = input("Senha: ")

    if senha == usuario["senha"]:
        print("Login OK")
        banco(usuario)
    else:
        print("Senha errada")

# -----------------------------

def register():
    contas = carregar_contas()

    nome = input("Nome: ")
    cpf = input("CPF: ")
    senha = input("Senha: ")

    contas.append({
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "saldo": 0
    })

    salvar_contas(contas)

    print("Conta criada!")

# -----------------------------

def banco(usuario):
    contas = carregar_contas()

    print(f"\nSaldo atual: {usuario['saldo']}")

    valor = float(input("Depositar: "))
    usuario["saldo"] += valor

    salvar_contas(contas)

    print("Novo saldo:", usuario["saldo"])

# -----------------------------

inicio()