a = [10, 31, 25, 14]

for x in a:
    print(x)

print('#' * 20)

for i in range(len(a)):
    print(a[i])

print('#' * 20)

print(a)
for i in range(len(a)):
    a[i] = a[i] + 5

print(a)