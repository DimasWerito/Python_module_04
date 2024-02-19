"""
CHAT GPT
У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. 
Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, 
якщо необхідно сплатити за рахунками. Напишіть функцію amount_payment, 
яка приймає на вхід список платежів, підсумовує додатні значення та повертає суму платежу наприкінці місяця.
"""


def amount_payment(payments):
    total_payment = sum(payment for payment in payments if payment > 0)
    return total_payment
payments = [500, 200]
print(amount_payment(payments))
    