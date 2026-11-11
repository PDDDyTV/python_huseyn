def rect_pc(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    p = 2 * (a + b)
    s = a * b
    return (p, s)


for i in range(3):
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    print(rect_pc(x1, y1, x2, y2))
