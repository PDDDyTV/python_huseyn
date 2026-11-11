import math

def cmp_abs_sin(a, b):
    sa = abs(math.sin(math.radians(a)))
    sb = abs(math.sin(math.radians(b)))
    if sa > sb: return 1
    if sa < sb: return -1
    return 0

a=float(input("введите первый угол"))
b=float(input("введите второй угол"))
print(cmp_abs_sin(a,b))