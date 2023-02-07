r1 = float(input('insert a length of a segment: '))
r2 = float(input('insert a length of a segment: '))
r3 = float(input('insert a length of a segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\33[0:30:43mestas retas formam um triângulo!\33[m')
else:
    print('\33[0:30:43mestas retas não formam um triângulo!\33[m')

print('\33[0:30:45mE ASSIM SE MUDA A COR DAS LETRAS E FUNDOS\33[m')

#também é possível colocar a cor dentro de uma variável para ficar mais facil
#de printar ela, deve se usar chaves e aspas para usá-la. Pode ser uma lista tbm
