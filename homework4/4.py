a = [10, 20, 30, 40]

for i in range(0, len(a), 2):
   a[i], a[i+1] = a[i+1], a[i]

print(a)
