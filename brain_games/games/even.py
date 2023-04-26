import random

from brain_games.engine import play_game

# Название игры
GAME_NAME = 'Answer "yes" if the number is even, otherwise answer "no".'

# Диапазон чисел из которых будут браться псевдослучайные числа для вопросов
MIN_NUMBER = 1
MAX_NUMBER = 30


def create_question_with_right_answer():
    """ Создаёт вопрос для задания и
    возвращает его вместе с верным ответом """

    # Берём случайное число
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    # "Вычисляем" правильный ответ
    right_answer = "yes" if number % 2 == 0 else "no"
    return f"{number}", right_answer


def start_game():
    play_game(GAME_NAME,
              create_question_with_right_answer)
