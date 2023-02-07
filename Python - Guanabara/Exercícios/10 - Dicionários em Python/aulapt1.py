tupla = ()
lista = [] #ou list()
dicionário = {} #ou dict()

dicionário['nome'] = 'Pedro'
print(dicionário) #{'nome': 'Pedro'}
dicionário['idade'] = 29
print(dicionário.values()) #dict_values(['Pedro', 29])
del dicionário['idade']
print(dicionário.values()) #dict_values(['Pedro'])
print(dicionário.keys()) #dict_keys(['nome'])
print(dicionário.items()) #dict_items([('nome', 'Pedro')])
dicionário['idade'] = 30
dicionário['sexo'] = 'Masculino'
for k, v in dicionário.items():
    print(f'O {k} é {v}')
#O nome é Pedro
#O idade é 30
#O sexo é Masculino
for k in dicionário.items():
    print(k)
#('nome', 'Pedro')
#('idade', 30)
#('sexo', 'Masculino')
'''Listas podem conter dicionários e vice-versa, o mesmo vale com tuplas'''