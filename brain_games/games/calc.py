import operator
import random

from brain_games.engine import play_game

# Название игры
GAME_NAME = 'What is the result of the expression?'

# Диапазон чисел из которых будут браться псевдослучайные числа для вопросов
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_right_answer(operand, first_number, second_number):
    """
    Принимет математическое действие и два числа.
    Возвращает результат переданной операции с переданными числами.
    """
    return operand(first_number, second_number)


def create_question_with_right_answer():
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
    number_a = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_b = random.randint(MIN_NUMBER, MAX_NUMBER)
    # Считаем правильный ответ
    right_answer = get_right_answer(operands[operand], number_a, number_b)
    return f"{number_a} {operand} {number_b}", right_answer


def start_game():
    play_game(GAME_NAME, create_question_with_right_answer)
