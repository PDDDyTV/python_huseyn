a = [1, 2, 2, 3, 4, 1]
a.append(-float('inf'))
m = 0
max = 0
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        m += 1
    else:
        if m > max:
            max = m

        m = 1

print(max)
