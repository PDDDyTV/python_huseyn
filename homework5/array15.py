n = int(input("Введите n: "))

lst = []
a = []
b = []
for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(0, n, 2):
    a.append(lst[i])

for i in range(1, n, 2):
    b.append(lst[i])


print(a)
b.reverse()
print(b)