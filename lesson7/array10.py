n = int(input("введите n"))

lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

even = []
odd = []

for i in range(n):
    if lst[i] % 2 == 0:
        even.append(lst[i])
    if lst[i] % 2 != 0:
        odd.append(lst[i])

print(even)
print(odd.reverse())
