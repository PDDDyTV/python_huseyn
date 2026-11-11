def even(k):
    if k % 2 == 0:
        return True
    else:
        return False


for i in range(10):
    a = int(input("Enter a:"))
    print(even(a),sep="/n")
