notas_alunos = {}

notas_alunos['Daniel'] = [3, 5, 6]
notas_alunos['Danilo'] = [4, 7, 2]
notas_alunos['Fernanda'] = [4, 7, 2]

for nome, notas in notas_alunos.items():
    print(nome, notas)

media_alunos = {}

for nome, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    media_alunos[nome] = media

for nome, media in media_alunos.items():
    print(f"Aluno: {nome} Media: {media:.1f}")