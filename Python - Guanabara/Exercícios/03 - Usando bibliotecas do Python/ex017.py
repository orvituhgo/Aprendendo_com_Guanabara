import math
line = 40 * '-'
print(line)
print('HIPOTENUSA CALCULATOR'.center(40, '-'))
print(line)
c1 = float(input('write the first measure of "cateto": '))
c2 = float(input('write the second measure of "cateto": '))
h = math.sqrt(c1**2+c2**2)
print('you said the "catetos" measure {:.2f} and {:.2f} so the "hipotenusa" is {:.2f}'.format(c1, c2, h))
