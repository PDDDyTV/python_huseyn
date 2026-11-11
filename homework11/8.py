s = input("Введите строку: ")
k = str()
for i in range(len(s)):
    if s[i] != " ":
        k = k + s[i]

    else:
        print(k)
        break
