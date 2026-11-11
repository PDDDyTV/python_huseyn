def is_square(k):
    if k * k == k ** 2:
        return True
    else:
        return False

for i in range(10):
    a = float(input("Enter a:"))
    print(is_square(a),sep="/n")