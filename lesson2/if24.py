import math

x = float(input())
f = 0

if x <= 0:
    f = 6 - x
else:
    f = 2 * math.sin(x)

print(f)
