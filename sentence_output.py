import time


def sentence_output_input(sentence: str) -> (float, str):
    """
    Функция для отображения предложения и получение ввода от пользователя

    Используется функция для генерации предложения, которое выводится пользователю.
    У пользователя запрашивается ввести предложение.
    Здесь замеряется время ввода.
    Args:
        sentence - сгенерированное предложение
    Returns:
        session_time - float - время затраченное на ввод в секундах
        user_input - str - введенная пользователем строка

    """
    print(f':: {sentence}')

    start_time = time.time()
    user_input = input(':: ')
    end_time = time.time()

    session_time = end_time - start_time

    return session_time, user_input
