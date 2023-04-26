import random

from brain_games.engine import play_game

# Название игры
GAME_NAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# Диапазон чисел из которых будут браться псевдослучайные числа для вопросов
MIN_NUMBER = 1
MAX_NUMBER = 200


def isprime(num):
    if num > 1:
        for n in range(2, num // 2 + 1):
            if num % n == 0:
                return False
        return True
    else:
        return False


def create_question_with_right_answer():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """

    # Берём случайное число
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    # "Вычисляем" правильный ответ
    right_answer = "yes" if isprime(number) else "no"
    return f"{number}", right_answer


def start_game():
    play_game(GAME_NAME,
              create_question_with_right_answer)
