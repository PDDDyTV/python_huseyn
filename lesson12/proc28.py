def is_prime(n):
    if n < 2:
        return False
    if n > 1:
        for j in range(2, n):
            if n % j == 0:
                return False
            else:
                return True


k = 0

for i in range(10):
    n = int(input("n="))
    if is_prime(n):
        k += 1

print(k)
