from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio == fim:
        print('INICIO igual ao FIM', end=' ')
    elif inicio > fim and passo < 0:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio = inicio + passo
            sleep(0.15)
    elif inicio < fim and passo > 0:
        while inicio <= fim:
            print(inicio, end=' ')
            inicio = inicio + passo
            sleep(0.2)
    elif inicio > fim and passo > 0:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio = inicio - passo
            sleep(0.15)
    print()

contador(0, 10, 1)
contador(10, 0, 1)
contador(inicio = int(input('Início: ')),
         fim = int(input('Fim: ')),
         passo = int(input('Passo: ')))

