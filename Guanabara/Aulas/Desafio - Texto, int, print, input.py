nome = input('Qual é o seu nome? ')
print('Olá, ', nome, '! Seja bem-vindo!')
dia = input('Qual é o dia do seu aniversário? ')
mes = input('E o mês? ')
ano = input('E o ano? ')
print('Você nasceu em ' + dia + '/' + mes + '/' + ano)
n1 = int(input('digite um número: '))
n2 = int(input('digite mais um número: '))
resultado = n1+n2
print('A soma dos números escolhidos é: ', resultado)

#pode também ser usado um comando muito mais eficiente para múltiplas variáveis

print('A soma entre {} e {} vale {} '.format(n1, n2, resultado))
