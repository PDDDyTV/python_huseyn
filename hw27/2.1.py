import math

x = float(input("Введите x: "))
y = float(input("Введите y: "))

res = round(math.sqrt(x ** 2 + y ** 2), 2)
print(f"Результат: {res}")
