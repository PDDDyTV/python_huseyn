import math


def solve_quadratic(a, b, c):
    if (a == 0):
        return "not quadratic"
    else:
        return ((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a), (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a))


a = int(input("введите чисо a"))
b = int(input("введите чисо b"))
c = int(input("введите чисо c"))
print(solve_quadratic(a, b, c))
