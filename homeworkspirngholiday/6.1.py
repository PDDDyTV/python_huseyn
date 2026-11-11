def count_uppercase(text):
    count = 0
    for c in text:
        if 'А' <= c <= 'Я' or 'A' <= c <= 'Z':
            count += 1
    return count


t = str(input("Введите строку: "))
print(count_uppercase(t))
