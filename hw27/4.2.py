def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


a = int(input("Введите перовое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print(min_of_three(a, b, c))
