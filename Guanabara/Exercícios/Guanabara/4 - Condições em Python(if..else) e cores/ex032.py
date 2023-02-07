from datetime import date

year = int(input('Insert a year (if you want inspect current year digit 0): '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{} é um ano bissexto'.format(year))
else:
    print('{} não é um ano bissexto'.format(year))
