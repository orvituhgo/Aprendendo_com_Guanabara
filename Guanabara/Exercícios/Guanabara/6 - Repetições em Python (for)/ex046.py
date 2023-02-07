from time import sleep

n = int(input('Selecione o tempo da contagem regressiva: '))

for c in range(0, n):
    print(n)
    n = n - 1
    sleep(1)
print("FELIZ ANO NOVO!")
