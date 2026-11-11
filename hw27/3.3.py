import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Два корня: x1 = {x1}, x2 = {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"Один корень: x = {x}")
else:
    print("Дискриминант отрицательный, действительных корней нет.")
