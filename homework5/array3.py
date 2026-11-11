n = int(input("Введите N: "))
a = float(input("Введите A: "))
d = float(input("Введите D: "))

lst = []

for i in range(n):
    x = a + i * d

    lst.append(x)

print(lst)