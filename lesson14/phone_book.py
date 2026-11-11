path_to_file = "Phone book.txt"

def show_book():
    with open(path_to_file, "r", encoding='utf-8') as file:
        print(file.read())
        print('\n')

def add_contact(name, phone_number):
    with open('Phone book.txt', 'a', encoding='utf-8') as file:
        row_to_write = name + "." + phone_number + '\n'
        file.write(row_to_write)

def show_menu():
    print("""Добро пожаловать в телефонную книгу!
Выберите действие:
1. Добавить 
2. Посмотреть контакты
3. Удалить контакт
4. Редактировать 
5. Очистить телефонную книгу
6. Выход
""")

def show_action():
    print("""Выберите действие:
1. Показать основное меню
2. Выход
""")



show_menu()
n_choose = int(input())

while True:
    if n_choose == 1:
        name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        add_contact(name, phone_number)
    elif n_choose == 2:
        show_book()
    elif n_choose == 3:
        pass
    elif n_choose == 4:
        pass
    elif n_choose == 5:
        with open(path_to_file, "w", encoding='utf-8') as file:
            file.write("")
    elif n_choose == 6:
        exit()

    show_action()
    action_num = int(input())
    if action_num == 1:
        show_menu()
        n_choose = int(input())
    elif action_num == 2:
        exit()
