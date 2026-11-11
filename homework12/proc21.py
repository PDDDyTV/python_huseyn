def sum_range(a, b):
    if a < b:
        return 0
    else:
        s = 0
        for i in range(a, b + 1):
            s += i
        return s


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print(sum_range(a, b))
print(sum_range(b, c))
