"""
CHAT GPT
Оцінка	Бали	Оцінка ECTS	Пояснення
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Реалізуйте дві функції. Перша буде використовуватись 
у бухгалтерії при розрахунку стипендії, 
get_grade приймає ключ у вигляді оцінки ECTS, 
і має повертати відповідну п'ятибальну оцінку (перший стовпчик таблиці). 
Друга get_description теж приймає ключ у вигляді оцінки ECTS, 
але повертатиме пояснення оцінки в текстовому форматі (останній стовпчик таблиці) 
і буде використана в електронній заліковій книжці студента. 
На відсутній ключ функції повинні повертати значення None .
"""


    
def get_grade(ects_grade):
    grades = {
        'A': 5,
        'B': 5,
        'C': 4,
        'D': 3,
        'E': 3,
        'FX': 2,
        'F': 1
    }
    return grades.get(ects_grade, None)

def get_description(ects_grade):
    descriptions = {
        'A': 'Perfectly',
        'B': 'Very good',
        'C': 'Good',
        'D': 'Satisfactorily',
        'E': 'Enough',
        'FX': 'Unsatisfactorily',
        'F': 'Unsatisfactorily'
    }
    return descriptions.get(ects_grade, None)

# Приклад використання
ects_grade = 'B'
print(get_grade(ects_grade))          # Виведе 5
print(get_description(ects_grade))   # Виведе 'Very good'
