def quater(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 4
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 2


for i in range(3):
    x = float(input("Enter x:"))
    y = float(input("Enter y:"))
    print(quater(x, y, sep="/n"))
