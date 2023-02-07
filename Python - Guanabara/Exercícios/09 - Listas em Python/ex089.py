from time import sleep

alunos = list()
estudante = list()
médias = list()
notas = list()
nome = list()
média = SN = aluno = 0

while True:
    nome.append(str(input('Digite o nome do aluno(a): ')))
    estudante.append(nome[:])
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota : ')))
    estudante.append(notas[:])
    médias.append((notas[0] + notas[1])/2)
    estudante.append(médias[:])
    alunos.append(estudante[:])
    estudante.clear()
    médias.clear()
    nome.clear()
    notas.clear()
    SN = str(input('Deseja continuar? [S/N]'))
    if SN in 'Nn':
        break
sleep(0.5)
print(50 * '=')
print('BOLETIM'.center(50, '-'))
print(50 * '=')
sleep(0.5)
print(f'{"ID":<5}{"ALUNO":<35}{"MÉDIA":>10}')
print(50 * '=')
for i in range(0, len(alunos)):
    print(f'{i:<5}{alunos[i][0][0]:<35}{alunos[i][2][0]:>10}')
print(50 * '=', '\n')
sleep(0.5)
while True:
    aluno = int(input('Digite o ID do aluno que deseja ver as notas (999 interrompe): '))
    if aluno == 999:
        print(50*'-')
        print('Desligando o programa')
        sleep(1)
        print(50*'-')
        break
    print(f'A notas de {alunos[aluno][0][0]} são: {alunos[aluno][1]}', '\n')
    print(50*'=')

