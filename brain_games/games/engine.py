import prompt


def welcome():
    """ Приветствует пользователя, возвращает его имя """
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name


def play_game(header, question_func, count=3):
    """ Основная функция движка игры. Принимает название игры,
    функцию создающую вопрос и кол-во вопросов (3 по-умолчанию)"""
    username = welcome()
    print(header)
    for i in range(count):
        # Вызываем функцию для получения текста вопроса и ответ
        question_text, right_answer = question_func()
        user_answer = ask_one_question(question_text)
        correct = check_answer(user_answer, right_answer, username)
        if not correct:
            return
    print(f"Congratulations, {username}!")


def check_answer(answer, right_answer, name):
    if answer == str(right_answer):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
              f"'{right_answer}'.\nLet's try again, {name}!")
        return False


def ask_one_question(question):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    return answer
