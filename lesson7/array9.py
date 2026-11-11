n = int(input("введите n"))

lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

even = []

for i in range(n):
    if lst[n-1-i] % 2 == 0:
        even.append(lst[n-1-i])

print(even)


