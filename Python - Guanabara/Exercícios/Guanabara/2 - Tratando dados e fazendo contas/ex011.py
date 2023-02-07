print('Paint Calculator \nsay the size of the wall: ')
hwall = float(input('heigth: '))
lwall = float(input('length: '))
vol_paint = (hwall*lwall)/2
print('you will need {:.3f} liters of paint.'.format(vol_paint.__ceil__()))
