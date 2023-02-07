print('-' * 50)
print('CAIXA ELETRÔNICO'.center(50, '-'))
print('-' * 50)
print('Notas disponíveis: R$50, R$20, R$10, R$5 e R$1')


saque = int(input('Digite quanto deseja sacar: '))
while saque <= 0:
    saque = int(input('Digite quanto deseja sacar: '))
notas50 = int(saque / 50)
resto50 = saque - notas50*50
notas20 = int(resto50 / 20)
resto20 = resto50 - notas20*20
notas10 = int(resto20 / 10)
resto10 = resto20 - notas10*10
notas5 = int(resto10 / 5)
resto5 = resto10 - notas5*5
notas1 = int(resto5)

print(f'''Você receberá:
{notas50} cédulas de R$50,00
{notas20} cédulas de R$20,00
{notas10} cédulas de R$10,00
{notas5} cédulas de R$5,00
{notas1} cédulas de R$1,00''')
