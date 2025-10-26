import os


def print_docs(directory):
    all_lines = os.walk(directory)
    for catalog in all_lines:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файл: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)



print_docs(r'D:\Warcraft 3 Frozen Throne\Errors')