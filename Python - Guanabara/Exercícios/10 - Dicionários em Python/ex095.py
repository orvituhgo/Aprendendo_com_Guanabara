from time import sleep
dados = dict()
ficha = list()
gols = list()
soma = 0

while True:
    dados['nome'] = str(input('Qual é o jogador? '))
    j = int(input('Quantos jogos jogou? '))
    for t in range(0, j):
        gol = (int(input(f'Quantos gols realizou na partida {t + 1}? ')))
        soma += gol  # poderia ser sum(gols) la em baixo fora desse laço
        gols.append(gol)
    dados['divgols'] = gols[:]
    dados['totgols'] = sum(gols)
    gols.clear()
    ficha.append(dados.copy())
    SN = str(input('Deseja continuar? [S/N]: '))
    if SN in 'Nn':
        break
print(f'{"No.":<5}{"Jogador":<10}{"Gols":^10}{"Total":^3}')
for p in range(0, len(ficha)):
    print(f"{p + 1:<5}{ficha[p]['nome']:<10}\t{ficha[p]['divgols']}\t{ficha[p]['totgols']:>5}")
print()
while True:
    resp = int(input('Deseja ver detalhes de qual jogador? (999 para parar): '))
    if resp == 999:
        break
    for p in range(0, len(ficha[resp-1]['divgols'])):
        print(f'No jogo {p + 1} fez {ficha[resp-1]["divgols"][p]}')
sleep(1)
print('>>>FINALIZANDO<<<')
