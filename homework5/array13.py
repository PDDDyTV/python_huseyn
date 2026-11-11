n = int(input("Введите n:"))

lst = []

for i in range(n):
    x = float(input())
    lst.append(x)

result = []

for j in range(n-1, -1, -2):
    y = lst[j]
    result.append(y)

print(result)

