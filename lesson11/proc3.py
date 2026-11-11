def mean(x, y):
    amean = (x + y) / 2
    gmean = (x + y) ** 0.5
    return (amean, gmean)

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

print(mean(a, b))
print(mean(a, c))
print(mean(a, d))
