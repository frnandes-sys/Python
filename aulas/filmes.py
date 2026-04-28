filme1 = {'titulo': 'Vingadores: Ultimato', 'ano': 2020, 'genero': 'Ação', 'diretor': 'Alguem'}
filme2 = {'titulo': 'F1', 'ano': 2020, 'genero': 'Ação', 'diretor': 'Alguem'}
filme3 = {'titulo': 'Velozes e Furiosos 7', 'ano': 2020, 'genero': 'Ação', 'diretor': 'Alguem'}

filmes = [filme1, filme2, filme3]

def exibir_info(filme):
    print(f"Filme: {filme['titulo']}")
    print(f"Ano: {filme['ano']}")
    print(f"Gênero: {filme['genero']}")
    print(f"Diretor {filme['diretor']}")
    print()

def visualizar_filmes():
    print("Lista de Filmes:")
    print()
    for filme in filmes:
        exibir_info(filme)

visualizar_filmes()