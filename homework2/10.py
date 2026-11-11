import math

a = float(input("Введите число :"))
if a >= -1 and a <= 1:
    a = math.cos(a)
    print(a*180.0/math.pi)
else:
    print("ERROR")
