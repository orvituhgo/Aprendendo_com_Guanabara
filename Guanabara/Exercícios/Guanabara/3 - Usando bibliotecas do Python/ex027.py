name = input('Write your name: ').strip().lower().split()
l = len(name)

print('Your first name is: {}'.format(name[0]))
print('Your last name is: {}'.format(name[l-1]))
