import random

from brain_games.cli import welcome_user
from brain_games.service import ask_question, check_answer


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1, 30)
        answer = ask_question(number)
        correct = check_answer(answer, "yes" if number % 2 == 0 else "no", name)
        if not correct:
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
