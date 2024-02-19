"""

GPT

Створіть функцію parse_args, яка повертає рядок, 
складений з аргументів командного рядка, розділених пробілами. 
Наприклад, якщо скрипт був викликаний командою: python run.py first second, 
то функція parse_args повинна повернути рядок наступного виду 'first second'.
"""


import sys

def parse_args():
    args = sys.argv[1:]
    return ' '.join(args)

# Приклад використання
args_string = parse_args()
print(args_string)
