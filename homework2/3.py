import math

a = float(input("Введи первый угол: "))
b = float(input("Введи второй угол: "))
sin1 = abs(math.sin(a))
sin2 = abs(math.sin(b))
if sin1 > sin2:
    print("синус первого угла больше")
if sin1 < sin2:
    print("синус второго угла больше")
if sin1 == sin2:
    print("синус углов равны")
