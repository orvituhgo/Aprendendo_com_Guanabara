aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Nota: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'reprovado'
elif 10 <= aluno['media'] >= 5:
    aluno['situacao'] = 'aprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')
