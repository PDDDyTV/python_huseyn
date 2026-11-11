def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > b and c > a:
        return c


n = int(input("введите n"))
print(max_of_three(a, b, c))
