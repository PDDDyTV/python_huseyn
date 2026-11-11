m = int(input("Введите номер месяца: "))
y = int(input("Введите год: "))
if m in [1, 3, 5, 7, 8, 10, 12]:
    d = 31
elif m in [4, 6, 9, 11]:
    d = 30
elif m == 2:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        d = 29
    else:
        d = 28
