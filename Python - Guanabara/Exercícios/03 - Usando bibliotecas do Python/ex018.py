import math

deg = math.radians(float(input('write a degree to know sin cos and tan: ')))
print('degree = {:.2f}, sin = {:.2f}, cos = {:.2f} and tan = {:.2f}'.format(deg, math.sin(deg), math.cos(deg),
                                                                            math.tan(deg)))
# math.radians -> degree to radian
# math.degree -> radian to degree
# math.sin or .cos or .tan always calculate in radians
