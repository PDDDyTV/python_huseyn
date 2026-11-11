n = int(input("Введите n: "))

lst = []

for i in range(n):
    x = float(input())
    lst.append(x)

k = 0

for i in range(n):
    if lst[i] % 2 != 0:
        print(lst[i])
        k = k + 1

print("Количество - " + str(k))