N = int(input("Введите число N (от 1 до 10): "))
f = 1

for i in range(1, N + 1):
    f *= i

print(f"Факториал числа {N} равен {f}")
