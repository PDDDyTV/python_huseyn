n = int(input("Введите N:"))

lst = []

for i in range(n):
    a = 2 ** (i+1)

    lst.append(a)

print(lst)
