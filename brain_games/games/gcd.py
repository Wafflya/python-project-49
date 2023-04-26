import random
from math import gcd

from brain_games.engine import play_game

# Название игры
GAME_NAME = 'Find the greatest common divisor of given numbers.'

# Диапазон чисел из которых будут браться псевдослучайные числа для вопросов
MIN_NUMBER = 1
MAX_NUMBER = 150


def create_question_with_right_answer():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """

    # Берём 2 случайных числа
    number_a = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_b = random.randint(MIN_NUMBER, MAX_NUMBER)
    # "Вычисляем" правильный ответ
    right_answer = gcd(number_a, number_b)
    return f"{number_a} {number_b}", right_answer


def start_game():
    play_game(GAME_NAME,
              create_question_with_right_answer)
