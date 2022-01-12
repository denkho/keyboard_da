from get_sentence import get_sentence, select_language, open_file
import pytest
from unittest.mock import patch


@pytest.mark.parametrize(
    'expression, result',
    [
        [['asd'], ['Asd asd asd.', 'Asd asd asd!', 'Asd asd asd?',
                   'Asd asd asd asd.', 'Asd asd asd asd?', 'Asd asd asd asd!']],
    ]
)
def test_get_sentence(expression, result):
    expression = get_sentence(expression)
    assert expression in result


@pytest.mark.parametrize(
    'expression, result',
    [
        [[], ValueError],
        ['string', TypeError],
        ['', ValueError],
        [None, ValueError],
        [2, TypeError],
    ]
)
def test_negative_get_sentence(expression, result):
    with pytest.raises(result):
        get_sentence(expression)


def test_select_language():
    with patch("builtins.input", return_value='ru'):
        assert select_language() == '../../../tasks/words/dict.txt.gz'


@pytest.mark.parametrize(
    'expression, result',
    [
        ['./not_exist_file.gz', FileNotFoundError],
    ]
)
def test_negative_open_file(expression, result):
    with pytest.raises(result):
        open_file(expression)
