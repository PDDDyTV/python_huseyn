n = int(input("введите n:"))
a = int(input("введите a:"))
b = int(input("введите b:"))

lst = [a, b]
for i in range(n):
    f = lst[i-2] + lst[i-1]
    lst.append(f)

print(lst)
