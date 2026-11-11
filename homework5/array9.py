n = int(input("Введите n: "))

lst = []
a = []
for i in range(n):
    x = float(input())
    lst.append(x)

k = 0

for i in range(n):
    if lst[i] % 2 == 0:
        a.append(lst[i])
        k = k + 1

a.reverse()
print(a)
print("Количество - " + str(k))
