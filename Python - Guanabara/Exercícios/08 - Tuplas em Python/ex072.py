tupla = ('um', 'dois', 'três', 'quatro', 'cinco'
         , 'seis', 'sete', 'oito', 'nove'
         , 'dez', 'onze', 'doze', 'treze'
         , 'quatorze', 'quinze', 'dezesseis'
         , 'dezesete', 'dezoito', 'dezenove')
t = int(input('Digite um número entre 0 e 20: '))
while t not in range(1, 20):
    t = int(input('Tente novamente. Digite um número '
                  'entre 0 e 20: '))
print(f'Você digitou {tupla[t-1]}')
