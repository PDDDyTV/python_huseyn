a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
else:
    max = c

print(f"Наибольшее число: {max}")
