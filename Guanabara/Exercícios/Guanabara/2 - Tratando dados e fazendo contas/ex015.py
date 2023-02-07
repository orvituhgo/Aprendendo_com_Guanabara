#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.

linha = 50 * 'X'
print(linha)
print('RENT CALCULATOR'.center(50, '-'))
print(linha)

print('To calculate the amount rent we need to know the information below.')
days = int(input('Say how many days you stayed with the car: '))
km = float(input('Say how many kilometers you drove with the car: '))
rent = days * 60 + km * 0.15
print('Per kilometer driven you pay R$0,15 and per day R$ 60. So you must pay {:.2f}'.format(rent))
