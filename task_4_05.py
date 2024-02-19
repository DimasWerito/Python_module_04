"""
GPT

У нас є список показників студентів групи – це список з отриманими балами з тестування. 
Необхідно поділити список на дві частини. 
Напишіть функцію split_list, яка приймає список (цілі числа), 
знаходить середнє значення бала у списку та ділить його на два списки. 
У перший потрапляють значення менше середнього, 
включаючи середнє значення, тоді як у другий — строго більше від середнього. 
Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
"""


def split_list(scores):
    if not scores:
        return [], []

    average_score = sum(scores) / len(scores)
    lower_scores = [score for score in scores if score <= average_score]
    higher_scores = [score for score in scores if score > average_score]

    return lower_scores, higher_scores