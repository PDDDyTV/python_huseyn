import math


def triangle_p(a, h):
    return a + 2 * math.sqrt((a / 2) ** 2 + h ** 2)


for i in range(3):
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    print(triangle_p(a, h))
