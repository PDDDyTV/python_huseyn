def prime_info(n):
    if n <= 1:
        return (False, None)

    for d in range(2, n):
        if n % d == 0:
            return (False, d)

    return (True, None)


n = int(input("введите число:"))
print(prime_info(n))
