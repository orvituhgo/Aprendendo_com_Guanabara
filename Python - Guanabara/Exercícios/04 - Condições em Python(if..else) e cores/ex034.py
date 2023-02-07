wage = float(input('say your wage to get a increase: '))

if wage > 1250:
    nwage = wage * 1.1
if wage <= 1250:
    nwage = wage * 1.15

print('your new wage is {:.2f}'.format(nwage))
