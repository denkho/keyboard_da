import gzip
import random


def get_sentence(words: list) -> str:
    """
    Функция get_sentence() генерирует предложение из списка words
    Args:
        words: список слов
    Returns:
        предложение в виде строки
    """
    if not words:
        raise ValueError
    elif type(words) != list:
        raise TypeError
    else:
        sentence_length = random.randint(3, 4)
        sign_end = random.choices('.!?', weights=[50, 25, 25])[0]
        sentence = ' '.join(random.choices(words, k=sentence_length)) + sign_end
        sentence = sentence[0].upper() + sentence[1:]
        return sentence


def open_file(path: str) -> list:
    """
    Функция open_file() открывает файл по пути (path) и преобразует его посторочно в список слов
    Args:
        path: путь к файлу
    Returns:
        список слов
    """
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        return f.read().splitlines()


def select_language():
    """
    Функция select_language() выбора языка из указанных в словаре paths
    Returns:
        путь к файлу, соответсвующему языковому коду
    """
    paths = {
        'ru': ['русский', 'dicts/dict_ru.txt.gz'],
        'en': ['английский', 'dicts/dict_en.txt.gz'],
    }
    while True:
        language = input('Выберите язык - {}:'.format(", ".join(f'{k} ({v[0]})' for k,v in paths.items())))
        if language in paths.keys():
            return paths[language][1]
