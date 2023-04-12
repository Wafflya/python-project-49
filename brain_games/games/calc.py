import operator
import random

from brain_games.games.engine import play_game


def create_question():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """

    # Доступные математические действия
    operands = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul
    }

    # Выбираем случайное математическое действие
    operand = random.choice(list(operands.keys()))
    # Берём 2 числа над которыми они будут проводиться
    number_a = random.randint(1, 20)
    number_b = random.randint(1, 20)
    # Считаем правильный ответ
    right_answer = operands[operand](number_a, number_b)
    return f"{number_a} {operand} {number_b}", right_answer


def main():
    play_game('What is the result of the expression?', create_question)
