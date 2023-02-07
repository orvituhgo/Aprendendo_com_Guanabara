from datetime import date

#nome, ano de nascimento, CTPS, ano da contratação, salário
dados = dict()

year = date.today().year

dados['nome'] = str(input(f'Nome: '))
dados['AnoNascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = year - dados['AnoNascimento']
dados['CTPS'] = int(input('Número da CTPS(0 se não tem): '))
if dados['CTPS'] != 0:
    dados['AnoContratacao'] = int(input('Ano da contratação: '))
    dados['Salário'] = int(input('Salário(reais): '))
    dados['AnoAposentadoria'] = 35 - (year - dados['AnoContratacao'])

for k, v in dados.items():
    print(f'{k} é igual a {v}')
