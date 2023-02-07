n = 0
s = 0
cont = 0
for c in range(1, 501, 2):
    n = n + 1
    if n % 3 == 0:
        s = s + c
        cont = cont + 1
print(s)
print(cont)
#questão com mtos erros na resolução