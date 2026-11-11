char = input("Введите один символ: ")
if len(char) > 0:
    code = ord(char[0])
    print(f"Код в Unicode: {code}")
    if 'A' <= char[0] <= 'Z':
        print("Символ является заглавной латинской буквой.")
    else:
        print("Символ НЕ является заглавной латинской буквой.")
