n = int(input("Введите n: "))
k = int(input("Введите k: "))
l = int(input("Введите l: "))
t = 0
p = 0
lst = []

for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(k, l, 1):
    t += lst[k + i - 1]
    p += 1
    t = t / p

print(t)
