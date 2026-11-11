def next_letter(ch):
    if ch == "z":
        return "a"
    if ch == "Z":
        return "A"
    if ((ord(ch) < 97 and ord(ch) > 122) or (ord(ch) < 65 and ord(ch) > 90)):
        return "ERROR"
    else:
        ch = ord(ch) + 1
        return chr(ch)

ch=str(input("введите букву"))
print(next_letter(ch))