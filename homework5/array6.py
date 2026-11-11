n = int(input("Введите n: "))

m = [1, 1]

for i in range(2, n):
    f = m[i - 1] + m[i - 2]
    m.append(f)


print(m)
