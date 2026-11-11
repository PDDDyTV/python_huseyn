import math

def acos_degrees(x):

    if (-1 <= x <= 1):
        return math.degrees(math.acos(x))
    else:
        raise ValueError("x должен быть в диапазоне [-1, 1]")

x=float(input("введите угол"))
print(acos_degrees(x))
