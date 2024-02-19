"""
CHAT GPT
При аналізі даних часто виникає необхідність позбавитися екстремальних значень, 
перш ніж почати працювати з даними далі. 
Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше та найменше значення, 
сортує його в порядку зростання і повертає змінений список як результат.
"""


def prepare_data(data):
    if len(data) < 3:
        return "Не вдалося обробити дані. Список має містити принаймні 3 елементи."

    # Видаляємо найбільше та найменше значення
    data.remove(max(data))
    data.remove(min(data))

    # Сортуємо список в порядку зростання
    data.sort()

    return data

# Приклад використання
data = [10, 5, 3, 8, 15, 2]
print(prepare_data(data))  # Виведе [3, 5, 8, 10]