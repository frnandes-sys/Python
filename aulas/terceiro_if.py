idade = int(input("Digite a idade:"))

if idade < 4:
        print("Idade não permitida.")
elif idade <= 12:
    adulto = str(input("Permissao do adulto? (sim/não): "))
    if adulto.lower() == "sim":
        print("Entrada Permitida.")
    else:
        print("Entrada não permitida.")
else:
    print("Entrada permitida")
