"""

GPT

Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. 
Функція повинна просканувати директорію path та повернути кортеж із двох списків. 
Перший — це список файлів усередині директорії, другий — список директорій.
"""


from pathlib import Path

def parse_folder(path):
    files = []
    directories = []

    for item in path.iterdir():
        if item.is_file():
            files.append(item.name)
        elif item.is_dir():
            directories.append(item.name)

    return files, directories

# Приклад використання
path = Path("шлях_до_директорії")
files, directories = parse_folder(path)
print("Файли:", files)
print("Директорії:", directories)
