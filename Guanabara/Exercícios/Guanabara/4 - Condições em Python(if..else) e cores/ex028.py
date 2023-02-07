import random
from time import sleep

sn = int(random.randint(0, 5))

print('The machine created a random number from 1'
      ' up to 5')

number = int(input('try to guess a secret number'
               ' that the machine created\n'))
sleep(2)
if sn == number:
    print('You right, the number is {}'.format(
        number))
else:
    print('You wrong, run out and try again.'
          ' The secret number is {}'.format(sn))
print(number)
print(sn)