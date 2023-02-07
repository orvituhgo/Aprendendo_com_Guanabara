import random

students = [input('first student: '), input('second student: '), input('third student: '), input('fourth student: ')]
random.shuffle(students)

print('the presetation order is: {}'.format(students))
