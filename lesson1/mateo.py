# Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

positive = 0
negative = 0

if a > 0:
    positive = positive + 1
elif a < 0:
    negative = negative + 1

if b > 0:
    positive = positive + 1
elif b < 0:
    negative = negative + 1

if c > 0:
    positive = positive + 1
elif c < 0:
    negative = negative + 1

print('Quantity of positive numbers: ', positive)
print('Quantity of negative numbers: ', negative)


