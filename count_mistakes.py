def count_mistakes(source_str: str, compare_str: str) -> int:
    """
    Функция count_mistakes() количество ошибок в compare_str в сравнении с source_str
    Посимвольно сравненивает строки и учитывает разницу длины строк
    Args:
        source_str: Исходная (правильная) строка
        compare_str: Сравниваемая с исходной строка

    Returns:
        cnt - Количество ошибок

    """
    cnt = sum(s1 != s2 for s1, s2 in zip(source_str, compare_str))
    cnt += abs(len(source_str) - len(compare_str))
    return cnt
