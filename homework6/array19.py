lst = []
ind = -1

for i in range(10):
    x = float(input())
    lst.append(x)

for i in range(1, 9):
    if (lst[0] < lst[i] and lst[i] < lst[9]):
        ind = ind + 1

print(k)
