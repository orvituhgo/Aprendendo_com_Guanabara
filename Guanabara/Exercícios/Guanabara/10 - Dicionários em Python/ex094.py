pessoas = list()
dados = dict()
somaIdade = numeroCadastros = 0
#cadastramento de pessoas (contando quantos cadastros e somando as idades e tratando erros)
while True:
    numeroCadastros += 1
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while dados['sexo'] not in 'MmFf':
        print('ERRO! Escolha M ou F')
        dados['sexo'] = str(input('Sexo [M/F]: '))
    dados['idade'] = int(input('Idade: '))
    somaIdade += dados['idade']
    pessoas.append(dados.copy())
    SN = str(input('Continuar cadastramento? [S/N] '))
    while SN not in 'SsNn':
        print('ERRO! Digite S ou N')
        SN = str(input('Continuar cadastramento? [S/N] '))
    if SN in 'Nn':
        break
mediaIdade = (somaIdade/numeroCadastros)
print(f'''\n- Foram cadastradas {numeroCadastros} pessoas.
- A média de idade é {mediaIdade:.2f}
- As mulheres cadastradas foram:''', end=' ')
#print de nome de pessoas
for p in pessoas:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')
print('\n')
print('Lista de pessoas acima da média:\n')
#print de pessoas acima da média em idade
for t in pessoas:
    if t['idade'] > mediaIdade:
        print(f'''Nome = {t["nome"]}; Sexo = {t["sexo"]}; Idade = {t["idade"]};\n''')
