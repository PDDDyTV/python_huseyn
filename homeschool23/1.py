a = list(input("введите список"))

for i in range(0, len(a)):
    if a[i] % 3 == 0:
        print(a[i])
