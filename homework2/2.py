import math

a = float(input("Введи угол: "))
print(math.sin(a))
if math.cos(a) == 0:
    print("ERROR")
else:
    print(math.cos(a))
