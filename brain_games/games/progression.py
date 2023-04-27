import random

from brain_games.engine import play_game

# Название игры
GAME_NAME = 'What number is missing in the progression?'

# Диапазон чисел из которых будут браться псевдослучайные числа для вопросов
MIN_START_NUMBER = 1
MAX_START_NUMBER = 100
STEP_RANGE = 10
NUMBERS_COUNT = 10


def get_right_answer(progression):
    """ Заменяет случайный элемент последовательности на .. и возвращает его """
    deleted_index = random.randint(0, NUMBERS_COUNT - 1)
    deleted_element = progression[deleted_index]
    progression[deleted_index] = ".."
    return deleted_element


def create_question_with_right_answer():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """
    # Берём 2 случайных числа, начало прогрессии и её шаг
    start = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = random.randint(-STEP_RANGE, STEP_RANGE)
    result_progression = [str(start + step * i) for i in range(NUMBERS_COUNT)]
    deleted_element = get_right_answer(result_progression)
    return " ".join(result_progression), deleted_element


def start_game():
    play_game(GAME_NAME, create_question_with_right_answer)
