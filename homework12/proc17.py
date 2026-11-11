def root_count(a, b, c):
    d = b * b - 4 * a * c
    if d == 0:
        return 1
    if d < 0:
        return 0
    if d > 0:
        return 2



for i in range(3):
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    print(root_count(a, b, c))
