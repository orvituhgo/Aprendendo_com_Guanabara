import random

students = [input('first student: '), input('second student: '), input('third student: '), input('fourth student: ')]

print('the winner of giveaway is: {}'.format(students[random.randint(0, 3)]))
