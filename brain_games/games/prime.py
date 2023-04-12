import random

from brain_games.games.engine import play_game


def isprime(num):
    if num > 1:
        for n in range(2, num // 2 + 1):
            if num % n == 0:
                return "no"
        return "yes"
    else:
        return "no"


def create_question():
    """ Создаёт вопрос для задания и возвращает его вместе с верным ответом """

    # Берём случайное число
    number = random.randint(1, 200)
    # "Вычисляем" правильный ответ
    right_answer = isprime(number)
    return f"{number}", right_answer


def main():
    play_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        create_question)
