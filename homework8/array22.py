n = int(input("Введите n: "))
k = int(input("Введите k: "))
l = int(input("Введите l: "))
t = 0
lst = []

for i in range(n):
    x = float(input())
    lst.append(x)

for i in range(n):
    if i < k or i > l:
        t += lst[i]

print(t)
