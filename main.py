from connection import cursor, connect
from commands import ClassComand, clear_console

comand = ClassComand

while True:
    selection = int(input('1 : Вывести все пароли\n2 : Получить пароль по id\n3 : Добавить пароль\n4 : Удалить пароль\n5 : Завершить программу\n'))

    match selection:
        case 1:
            clear_console()
            comand.get_all_passwords()
        case 2:
            clear_console()
            id = int(input("Введите id для получения записи: "))
            comand.get_a_password(id)
        case 3:
            clear_console()
            name = input('Введите название сайта/приложения: ')
            login = input('Введите логин: ')
            pas = input('Введите пароль: ')
            notes = input('Введите заметку. Если нет нажмите Enter:')

            comand.set_a_password(name, login, pas, notes)
        case 4:
            clear_console()
            id = int(input("Введите id для удаления записи: "))
            comand.remove_password(id)
        case 5: break


connect.close()
cursor.close()




