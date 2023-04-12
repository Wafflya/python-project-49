import random
from math import gcd
from brain_games.games.engine import play_game


def create_question():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """

    # Берём 2 случайных числа
    number_a = random.randint(1, 150)
    number_b = random.randint(1, 150)
    # "Вычисляем" правильный ответ
    right_answer = gcd(number_a, number_b)
    return f"{number_a} {number_b}", right_answer


def main():
    play_game('Find the greatest common divisor of given numbers.', create_question)

