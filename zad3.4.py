# Задание (3.4)
import random

def generate_expression():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    expression = f"{a} + {b} = "
    answer = a + b
    return expression, answer


correct_answers = 0
mistake_count = 0
while mistake_count < 3:
    expression, answer = generate_expression()
    user_answer = input(expression)
    if int(user_answer) == answer:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        mistake_count += 1

print(f"Игра окончена. Правильных ответов: {correct_answers}")
