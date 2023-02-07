import math

km = math.ceil(float(input('How many km you trip have? ')))

if km <= 200:
    print('This trip will costs {}'.format(km*0.50))
else:
    print('This trip will costs {}'.format(km*0.45))
#poderia ter colocar para definir a variável conforme a condição também.