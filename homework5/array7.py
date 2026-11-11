n = int(input("Введите n: "))

lst = []

for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(n):
    print(lst[n-1-i])

