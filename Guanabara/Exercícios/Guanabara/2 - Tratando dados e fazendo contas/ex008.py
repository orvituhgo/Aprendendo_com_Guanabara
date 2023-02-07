meter = float(input('insert a number of length to transform it in centimeters and millimeters: '))
centi = meter*10**2
milli = meter*10**3
print('you inserted {} is equal to {} cm or {} mm.'.format(meter, centi, milli))
