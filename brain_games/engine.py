import prompt

QUESTIONS_COUNT = 3


def play_game(header, question_func):
    """ Основная функция движка игры. Принимает название игры,
    функцию создающую вопрос и кол-во вопросов (3 по-умолчанию)"""
    print("Welcome to the Brain Games!")
    username = prompt.string('May I have your name? ')
    print(f"Hello, {username}")
    print(header)
    for i in range(QUESTIONS_COUNT):
        # Вызываем функцию для получения текста вопроса и правильный ответ
        question_text, right_answer = question_func()

        print(f"Question: {question_text}")
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(right_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{right_answer}'.\nLet's try again, {username}!")
            return
    print(f"Congratulations, {username}!")
