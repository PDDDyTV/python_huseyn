import math

degrees = float(input("Введите угол в градусах: "))
radians = math.radians(degrees)

sin = math.sin(radians)
cos = math.cos(radians)
val = sin ** 2 + cos ** 2

print(f"sin^2(alpha) + cos^2(alpha) = {val}")
