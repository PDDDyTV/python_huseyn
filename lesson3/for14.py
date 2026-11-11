n = int(input("N=         "))

c = 0
a = 1.1

for i in range(n):
    c = c + a
    a = (a + 0.1) * -1
print(f"The answer is:{c}")
