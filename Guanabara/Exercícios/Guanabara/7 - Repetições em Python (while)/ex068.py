from random import randint
v = 0
print('Vamos jogar IMPAR ou PAR:')
while True:
    j = int(input('Digite um número: '))
    c = randint(0, 10)
    ip = str(input('Quer I ou P? ')).strip().upper()
    if ((j + c) % 2) == 0 and ip == 'P':
        print(f'''Você venceu!
Vamos jogar novamente?
A soma dos números era {j + c}''')
        v += 1
    elif ((j + c) % 2) != 0 and ip == 'I':
        print(f'''Você venceu!
Vamos jogar novamente?
A soma dos números era {j + c}''')
        v += 1
    elif ((j + c) % 2) != 0 and ip != 'I':
        break
    elif ((j + c) % 2) == 0 and ip != 'P':
        break
print(f'Você perdeu depois de ganhar {v} seguidas!'
f'\nA soma dos números era {j + c}')
