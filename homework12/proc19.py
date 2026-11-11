def ring_s(r1, r2):
    return 3.14 * (r1 ** 2 - r2 ** 2)


for i in range(3):
    r1 = float(input("Enter r1: "))
    r2 = float(input("Enter r2: "))
    print(ring_s(r1, r2))
