def code_to_printable(n):
    if (32 <= n <= 126):
        return n
    raise ValueError(f"Код {n} не подходит условиям")


n = int(input("введите число "))
print(code_to_printable(n))


def printable_to_code(ch):
    if len(ch) == 1:
        return ch
    raise ValueError(f"'{ch}' не соответствует условию")


ch = str(input("введите число 2 "))
print(printable_to_code(ch))
