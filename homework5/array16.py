n = int(input("Введите n: "))

lst = []
a = []
for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(n // 2):
    a.append(lst[i])
    a.append(lst[n - i - 1])

if n % 2 != 0:
    a.append(lst[n // 2])

print(a)
