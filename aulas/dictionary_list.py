# names = {
#     'Maria': 30,
#     'Daniel': 18,
#     'Paulo': 20,
# }

# # for user, idade in names.items():
# #     print(user, idade)
#

# print(names.get('Daniel'))

user = {
    'nome': 'Daniel',
    'idade': '18',
    'cidade': 'Simoes Filho',
}

name = user.get('nome')
years = user.get('idade')
city = user.get('cidade')

print(f"Nome: {name}")
print(f"Idade de {name}: {years}")
print(f"Mora em: {city}")
