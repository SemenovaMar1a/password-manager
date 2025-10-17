import os
from connection import cursor, connect
from secretkey.secret import cipher

class ClassComand:
    """Команды управления менеджером паролей"""

    def get_all_passwords():
        """Вывод всех паролей в таблице"""

        cursor.execute("SELECT id, service_name, login, password, notes FROM password_manager;")
        rows = cursor.fetchall()

        print('ID', '|', 'Название сайта', '|', 'Логин       ', '|', 'Пароль', '|', 'Заметка                   ', '|')
        print('-' * 75)
        for i in rows:
            print(
                f"{i[0]:<2} | {i[1]:<14} | {i[2] if i[2] else '-': <13}| {'*****':<6} | {i[4] if i[4] else '-':<26} |")


    def get_a_password(id):
        """Вывод конкретного пароля по id"""

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

    def set_a_password(name, login, pas, notes):
        """Создание нового пароля"""

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

    def remove_password(id):
        """Удаление пароля по id"""

        cursor.execute("DELETE FROM password_manager WHERE id = %s", (id,))
        connect.commit()

def clear_console():
    """Очищение консоли"""
    
    if os.name == 'nt':
        os.system('cls')

