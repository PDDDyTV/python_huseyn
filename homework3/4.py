def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"

    if a * a + b * b == c * c:
        return "right"
    elif a * a + b * b > c * c:
        return "acute"
    else:
        return "obtuse"


k = int(input("Введите число"))
l = int(input("Введите число"))
m = int(input("Введите число"))
print(triangle_type(k, l, m))
