nota1 = float(input('Nota 1 do aluno: '))
nota2 = float(input('Nota 2 do aluno: '))

média = (nota1+nota2)/2

if média <6:
    print('Sua nota foi menor que 6, você precisa estudar mais!')
elif média >= 6 and média < 7.5:
#elif 7,5 > média >= 6 (outra opção)
    print('Você não reprovou mas precisa estudar um pouco mais!')
else:
    print('Parabéns sua nota está ótima!')
