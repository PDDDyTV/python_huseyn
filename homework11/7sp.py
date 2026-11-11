s = input("Введите строку: ")
k = str()
for i in range(len(s)):
    if s[i] != " ":
        o = i
        break

for j in range(len(s)):
    if s[-j] != " ":
        p = j
        break

print(s[o:len(s) - p + 1])
