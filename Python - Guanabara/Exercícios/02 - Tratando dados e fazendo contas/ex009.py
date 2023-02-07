n = 1
n1 = int(input('write a number: '))
print('you wrote {}, follow the mutiplies until/up to 10'.format(n1))
print('-' *40)
while n <= 10:
    print('your number multiply by {} is equal {}'.format(n, n1*n))
    n = n + 1
print('-' *40)
