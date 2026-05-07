def ler_arquivo():
    with open('text.html', 'r') as archive:
        conteudo = archive.read()
        print("Conteudo do arquivo 'text.html'\n")
        print(conteudo)

def gravar_arquivo():
    with open('text.html', 'a') as archive:
        conteudo = input("Digite oque quer adicionar ao arquivo, ou 'fim' para sair: ")
        archive.write("\n" + conteudo)

gravar_arquivo()
ler_arquivo()