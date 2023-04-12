import random

from brain_games.games.engine import play_game


def create_question():
    """ Создаёт вопрос для задания и
    возвращает его вместе с верным ответом """

    # Берём случайное число
    number = random.randint(1, 30)
    # "Вычисляем" правильный ответ
    right_answer = "yes" if number % 2 == 0 else "no"
    return f"{number}", right_answer


def main():
    play_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        create_question)
