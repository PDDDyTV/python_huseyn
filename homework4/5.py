a = list(map(int, input("Введите числа через пробел: ").split()))

min1 = float('inf')
min2 = float('inf')

for n in a:
    if n < min1:
        min2 = min1
        min1 = n
    elif n < min2:
        min2 = n

print(min1, min2)
