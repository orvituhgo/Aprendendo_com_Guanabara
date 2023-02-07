from datetime import date

anoatual = date.today().year
anonascimento = int(input('Digite o ano de nascimento: '))

def vota(ano):
    vota = ''
    idade = anoatual - ano
    if idade >= 18 and idade < 65:
        vota = f'Você tem {idade} anos: VOTO OBRIGATÓRIO'
    elif (idade < 18 and idade >= 16) or idade >= 65:
        vota = f'Você tem {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        vota = f'Você tem {idade} anos: VOTO PROIBIDO'
    return vota

print(vota(anonascimento))
