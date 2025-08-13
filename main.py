import os
from cryptography.fernet import Fernet
import psycopg2


with open("secret.txt", "rb") as f:
    key = f.read().strip()

cipher = Fernet(key)

connect = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='623528',
    host='localhost',
    port='5432'
    )

cursor = connect.cursor()


def clear_console():
    if os.name == 'nt':
        os.system('cls')


print('Действия:')
print('1 : Вывести все пароли\n2 : Получить пароль по id\n3 : Добавить пароль\n4 : Удалить пароль')

while True:
    number = input("Выбирите цифру действия (или 'exit' для выхода): ")

    if number.lower() == 'exit':
        print('Программа завершина')
        break

    if number == 'clear':  # Если введена команда "clear", очищаем консоль
        clear_console()
        print('Действия:')
        print('1 : Вывести все пароли\n2 : Получить пароль по id\n3 : Добавить пароль\n4 : Удалить пароль')

    if number == "1":
        cursor.execute("SELECT id, service_name, login, password, notes FROM password_manager;")
        rows = cursor.fetchall()

        print('ID', '|', 'Название сайта', '|', 'Логин       ', '|', 'Пароль', '|', 'Заметка                   ', '|')
        print('-' * 75)
        for i in rows:
            print(
                f"{i[0]:<2} | {i[1]:<14} | {i[2] if i[2] else '-': <13}| {'*****':<6} | {i[4] if i[4] else '-':<26} |")

    if number == '2':
        id = int(input("Введите id для получения записи: "))

        cursor.execute("SELECT * FROM password_manager WHERE id = %s", (id,))
        result = cursor.fetchone()

        if result:
            encrypted_password = result[3].encode('utf-8')
            try:
                decrypted_password = cipher.decrypt(encrypted_password).decode('utf-8')

                print("Запись найдена:")
                print(f"ID: {result[0]}")
                print(f"Имя сайта: {result[1]}")
                print(f"Логин: {result[2]}")
                print(f"пароль: {decrypted_password}")
            except Exception:
                print("Ошибка при расшифровке пароля")
        else:
            print("Запись не найдена.")

    if number == "3":
        name = input('Введите название сайта/приложения: ')
        login = input('Введите логин: ')
        pas = input('Введите пароль: ')
        notes = input('Введите заметку. Если нет нажмите Enter:')

        # Шифрование пароля
        cipher_text = cipher.encrypt(pas.encode('utf-8')).decode('utf-8')

        cursor.execute("""
        INSERT INTO password_manager (service_name, login, password, notes)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """, (name, login, cipher_text, notes))

        new_id = cursor.fetchone()[0]
        print(f"Запись добавлена, id = {new_id}")

        connect.commit()
        

    if number == '4':
        id = int(input("Введите id для удаления записи: "))
        cursor.execute("DELETE FROM password_manager WHERE id = %s", (id,))
        connect.commit()

connect.close()
cursor.close()




