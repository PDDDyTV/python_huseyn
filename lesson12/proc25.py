import math

def is_square(k):
    if k ** 0.5 == int(k ** 0.5):
          return True
    else:
        return False

l = 0

for i in range(10):
    n = int(input("n="))
    if is_square(n):
        l += 1

print(l)