a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
d = int(input("Fourth number: "))

if a==b==c:
    print("Четыре")

if(a!=b and a!=c and a!=d):
    print("1")
if (b != a and b != c and b != d):
    print("2")
if (c != b and c != a and c != d):
    print("3")
if (d != b and d != c and d != a):
    print("4")