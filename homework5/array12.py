n = int(input("Введите n: "))

lst = []
for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(0, n, 2):
    print(lst[i])
