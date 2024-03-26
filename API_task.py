# В даному випадку використоується функція "os.listdir()", яка є частиною
# модуля "os". Ця функція представляє API операційної системи для отримання
# списків файлів та папок у зазначеній директорії.

import os


def list_directory(directory_path, encoding='utf-8'):
    files = os.listdir(directory_path)

    for file_name in files:
        print(file_name.encode(encoding).decode(encoding))


list_directory("D:\\Python Practiсe")
