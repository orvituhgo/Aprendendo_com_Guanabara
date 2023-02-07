para = False
homens = fmenos20 = mais18 = 0
while not para:
    s = ''
    i = 0
    while s != 'M' and s != 'F':
        s = input('Sexo [M/F]: ').strip().upper()
        if s == 'M' or s == 'F':
            break
        print('Digite conforme indicado')
    while i <= 0:
        i = int(input('Idade: '))
        if i > 0:
            break
        print('Digite uma idade possível.')
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        fmenos20 += 1
    if i > 18:
        mais18 += 1
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    if c == 'N':
        para = True
    s = ''
    i = 0
print(f'''FORAM CADASTRADOS:
{homens} homem(ns)
{fmenos20} mulher(es) com menos de 20 anos
{mais18} pessoa(s) com mais de 18 anos''')
