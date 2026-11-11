a = [2, 5, 1, 4, 3, 3, 5, 10]

print(f"Before: {a}")

for i in range(0, len(a), 2):
    swap = a[i]
    a[i] = a[i + 1]
    a[i + 1] = swap

print(f"After: {a}")

