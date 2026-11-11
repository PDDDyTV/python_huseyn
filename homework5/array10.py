n = int(input("Введите n: "))

lst = []

for i in range(n):
    x = int(input())
    lst.append(x)

even = []
odd = []

for i in range(n):
    if lst[i] % 2 == 0:
        even.append(lst[i])
    else:
        odd.append(lst[i])

print(even)

odd.reverse()

print(odd)
