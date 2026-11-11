n = int(input("Введите n: "))
k = int(input("Введите k: "))

lst = []
for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(0, n, k):
    print(lst[i])
