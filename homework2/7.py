a = int(input("введите первый угол :"))
b = int(input("введите второй угол :"))
c = int(input("введите третий угол :"))
if a + b + c != 180:
    print("ERROR")
    exit()
elif b == 90 or a == 90 or c == 90:
    print("прямоугольный")
elif b > 90 or a > 90 or c > 90:
    print("тупоугольный")
elif b < 90 or a < 90 or c < 90:
    print("остроугольный")
