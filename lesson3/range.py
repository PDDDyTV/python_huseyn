n = int(input("введите n"))

s = 0
for i in range(n):
    s = s + 2 ** i

print("ответ", s)
