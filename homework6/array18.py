lst = []
k = 0

for i in range(10):
    x = float(input())
    lst.append(x)

for i in range(10):
    if lst[i] < lst[9]:
        k = lst[i]
        break

print(k)
