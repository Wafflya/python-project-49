import random

from brain_games.games.engine import play_game


def create_question():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """
    # Берём 2 случайных числа, начало прогрессии и её шаг
    start = random.randint(1, 100)
    step = random.randint(-10, 10)
    result_progression = [str(start + step * i) for i in range(10)]
    deleted_index = random.randint(0, 9)
    deleted_element = result_progression[deleted_index]
    result_progression[deleted_index] = ".."
    return " ".join(result_progression), deleted_element


def main():
    play_game('What number is missing in the progression?', create_question)
