v = float(input('insert the car velocity: '))
warning = (v - 80) *7

if v > 80:
    print("You were driving {:.2f}, it's over the limit of velocity."
          "\nSo you need pay {:.2f}".format(v, warning))
else:
    print('You were driving safety')
