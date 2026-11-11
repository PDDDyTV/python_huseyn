n = int(input("введите n"))
a = int(input("введите a"))
d = int(input("введите d"))

lst = []

for i in range(n):
    lst.append(a * d ** i)

print(lst)