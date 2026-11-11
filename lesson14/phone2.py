with open("phone.txt", "r", encoding='utf-8') as file:
    text = file.read()
    print(text)

with open("phone.txt", "w", encoding='utf-8') as file:
    file.write("Это наша новая запись")

