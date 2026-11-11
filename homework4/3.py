a = [1, 2, 3, 4, 5]
k = int(input("Введите число k: "))
b = a[-k:] + a[:-k]
print(b)