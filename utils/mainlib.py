from os import listdir, remove
from os.path import isfile, abspath, join, basename
from colorama import init, Fore, Back, Style


email_file = 'M:\\Programs\\workspace\\projects\\customs_app\\utils\\customs_emails.txt'
folder = 'M:\\Programs\\workspace\\projects\\customs_app\\copied_files\\'

init(convert=True)


def show_emails():
    with open(email_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        print(Fore.CYAN, '\nСписок адресов:', Style.RESET_ALL)
        [print(Fore.GREEN, num, '\t', line, Style.RESET_ALL) for num, line in enumerate(lines, 1)]


def add_email(email):
    with open(email_file, 'a', encoding='utf-8') as f:
        f.writelines(email + '\n')
        print(Fore.GREEN + '\'{}\' добавлен в список адресов.'.format(email), Style.RESET_ALL)


def delete_email(num_to_delete):
    email = None
    with open(email_file, 'r', encoding='utf-8') as f:
        lines = [line for line in f.readlines()]
    with open(email_file, 'w', encoding='utf-8') as f:
        for num, line in enumerate(lines, 1):
            if num == num_to_delete: email = line.strip('\n')
            if num != num_to_delete: f.write(line)
    if email:
        print(Fore.GREEN + '\'{}\' удален из списка адресов.'.format(email), Style.RESET_ALL)
    else:
        print(Fore.GREEN + 'Указанный адрес отсутствует в списке.', Style.RESET_ALL)


FILES = list()


def list_files():
    FILES.clear()
    for file in listdir(folder):
        abs_file = abspath(join(folder, file))
        if isfile(abs_file): FILES.append(abs_file)
    print(Fore.CYAN, '\nСписок файлов:', Style.RESET_ALL)
    [print(Fore.GREEN, num, '\t', basename(f), Style.RESET_ALL) for num, f in enumerate(FILES, 1)]


def delete_file(num_to_delete, all=True):
    if not all:
        filename = None
        for num, f in enumerate(FILES, 1):
            if num == num_to_delete:
                filename = f
                remove(f)
        if filename:
            print(Fore.GREEN + '\nФайл \'{}\' удален.'.format(basename(filename)), Style.RESET_ALL)
        else:
            print(Fore.GREEN + '\nТакого файла не существует.', Style.RESET_ALL)
    else:
        for f in FILES: remove(f)
        print(Fore.GREEN + '\nВсе файлы удалены.', Style.RESET_ALL)


def send_file():
    print('Файл отправлен')
    pass
