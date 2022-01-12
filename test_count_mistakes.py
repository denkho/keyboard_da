from count_mistakes import count_mistakes
import pytest


@pytest.mark.parametrize(
    'str1, str2, num',
    [
        ['Hello','hello', 1],
        ['Hello', 'heolo', 2],
        ['Hello', 'rtyui', 5],
        ['Hello', '', 5],
        ['Hello', 'Hello', 0],
        ['Hello', 'Heello', 3],
        ['Hello', 'Helo', 2],
    ]
)
def test_count(str1, str2, num):
    assert count_mistakes(str1, str2) == num
