from random import randint
linha = 40 * '-'
print(linha)
print('JOGO DA ADIVINHAÇÃO'.center(40, '='))
print(linha)
print('\nPensei em um número\nEm qual número eu pensei?')
pc = randint(0, 10)
tentativa = 1
jogador = int(input('Digite um número entre de 1 a 10:'))
while pc != jogador:
    tentativa += 1
    jogador = int(input('Digite um número entre de 1 a 10:'))
print('Você acertou pensei em {}'.format(pc))
print('Foram necessárias {} tentativas para acertar'
      .format(tentativa))
