'''n = s = 0
while n != 999:
    n = int(input('write a number: '))
    s += n
print(s-999)
'''

n = s = 0
n = int(input('write a number: '))
while n != 999:
    s += n
    n = int(input('write a number: '))
print(s)
