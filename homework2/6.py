a = str(input("введите символ :"))
if a == "z":
    print("a")
    exit()
if a == "Z":
    print("A")
    exit()
if ((ord(a) < 97 and ord(a) > 122) or (ord(a) < 65 and ord(a) > 90)):
    print("ERROR")
    exit()
else:
    a = ord(a) + 1
    print(chr(a))
