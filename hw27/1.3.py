x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
R = float(input("Введите радиус R: "))

square = x ** 2 + y ** 2
if square <= R ** 2:
    print("Точка находится внутри круга или на границе.")
else:
    print("Точка находится вне круга.")
