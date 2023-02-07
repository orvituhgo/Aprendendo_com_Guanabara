n1 = float(input('insert a number'))
n2 = float(input('insert a number'))
n3 = float(input('insert a number'))

highest = n1
if n2 > n1 and n2 > n3:
    highest = n2
if n3 > n1 and n3 > n2:
    highest = n3
lowest = n1
if n2 < n1 and n2 < n3:
    lowest = n2
if n3 < n1 and n3 < n2:
    lowest = n3
print('The highest number is {}'.format(highest))
print('The lowest number is {}'.format(lowest))