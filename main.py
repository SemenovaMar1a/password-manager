from connection import cursor, connect
from commands import ClassComand, clear_console

comand = ClassComand

while True:
    print('Действия:')
    print('1 : Вывести все пароли\n2 : Получить пароль по id\n3 : Добавить пароль\n4 : Удалить пароль')
    number = input("Выбирите цифру действия (или 'exit' для выхода): ")

    if number.lower() == 'exit':
        print('Программа завершина')
        break

    if number == 'clear':  # Если введена команда "clear", очищаем консоль
        clear_console() 
        print('Действия:')
        print('1 : Вывести все пароли\n2 : Получить пароль по id\n3 : Добавить пароль\n4 : Удалить пароль')

    if number == "1":
        clear_console()
        comand.get_all_passwords()

    if number == '2':
        clear_console()
        id = int(input("Введите id для получения записи: "))
        comand.get_a_password(id)

    if number == "3":
        clear_console()
        name = input('Введите название сайта/приложения: ')
        login = input('Введите логин: ')
        pas = input('Введите пароль: ')
        notes = input('Введите заметку. Если нет нажмите Enter:')

        comand.set_a_password(name, login, pas, notes)

    if number == '4':
        clear_console()
        id = int(input("Введите id для удаления записи: "))
        comand.remove_password(id)

connect.close()
cursor.close()




