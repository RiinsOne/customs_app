from utils import mainlib as lib
from colorama import init, Fore, Back, Style
from socket import gethostname
from os.path import basename


init(convert=True)

USER_CHOICE = """
Введите:
- 'le'  для просмотра списка адресов
- 'ae'  для добавления нового адреса
- 'de'  для удаления адреса
- 'lf'  для просмотра списка файлов
- 'df'  для удаления файла
- 'daf' для удаления всех файлов
- 'sf'  для отправки файла
- 'saf' для отправки всех файлов
- 'q'   для выхода

Ваш выбор: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'le':
            lib.show_emails()
        elif user_input == 'ae':
            prompt_add_email()
        elif user_input == 'de':
            prompt_delete_email()
        elif user_input == 'lf':
            lib.list_files()
        elif user_input == 'df':
            prompt_delete_file(set_all=False)
        elif user_input == 'daf':
            confirm = input('Для подтверждения введите \'y\'. Для возвращения в меню введите \'n\': ')
            if confirm.lower() == 'y':
                prompt_delete_file(set_all=True)
        elif user_input == 'sf':
            prompt_send_to_email(set_all=False)
        elif user_input == 'saf':
            prompt_send_to_email(set_all=True)
        else:
            print("Неизвестная комманда. Повторите ещё раз.")

        user_input = input(USER_CHOICE)


def prompt_add_email():
    print(Fore.GREEN + 'Введите новый адрес: ', Style.RESET_ALL, end='')
    email = input()
    lib.add_email(email)


def prompt_delete_email():
    print(Fore.GREEN + 'Для удаления адреса введите его порядковый номер: ', Style.RESET_ALL, end='')
    try:
        num = int(input())
        lib.delete_email(num)
    except ValueError:
        print(Fore.GREEN + 'Неверное значение.', Style.RESET_ALL)
    except IndexError:
        print(Fore.GREEN + '\nНеверное значение.', Style.RESET_ALL)


def prompt_delete_file(set_all=True):
    if not set_all:
        try:
            print(Fore.GREEN + 'Для удаления файла введите его порядковый номер: ', Style.RESET_ALL, end='')
            num = int(input())
            lib.delete_file(num, set_all)
        except ValueError:
            print(Fore.GREEN + 'Неверное значение.', Style.RESET_ALL)
        except IndexError:
            print(Fore.GREEN + '\nНеверное значение.', Style.RESET_ALL)
    else:
        lib.delete_file(1, set_all)


def prompt_send_to_email(set_all=True):
    if not set_all:
        try:
            lib.list_files()

            print(Fore.GREEN + '\nВыберите файл для отправки, укажите его порядковый номер: ', Style.RESET_ALL, end='')
            num_file = int(input())

            file = [lib.FILES[num_file-1]]
        except ValueError:
            print(Fore.GREEN + '\nНеверное значение.', Style.RESET_ALL)
            return
        except IndexError:
            print(Fore.GREEN + '\nНеверное значение.', Style.RESET_ALL)
            return
    else:
        file = lib.FILES

    try:
        emails = None
        email_file = 'C:\\OG\\workspace\\projects\\customs_app\\utils\\customs_emails.txt'

        lib.show_emails()
        print(Fore.GREEN + '\nВыберите адрес для отправки, укажите его порядковый номер: ', Style.RESET_ALL, end='')
        num_email = int(input())

        with open(email_file, 'r', encoding='utf-8') as f:
            emails = [line.strip() for line in f.readlines()]
        recipient = [emails[num_email-1]]
    except ValueError:
        print(Fore.GREEN + '\nНеверное значение.', Style.RESET_ALL)
    except IndexError:
        print(Fore.GREEN + '\nНеверное значение.', Style.RESET_ALL)

    lib.send_mail(
        send_from=gethostname(), send_to=recipient,
        subject=basename(file[0]), files=file, server=lib.SERVER_IP, port=lib.PORT
    )


if __name__ == '__main__': menu()
