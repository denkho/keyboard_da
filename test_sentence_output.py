import unittest
from unittest.mock import patch
from sentence_output import sentence_output_input


class SentenceOutputTestCase(unittest.TestCase):
    """
    Тесты для функции sentence_output_input() из sentence_output.py
    """

    def test_sentence_output_input(self):
        """Ввод-вывод строки работает верно"""
        user_input = ['Баклан жуть крепово']
        with patch('builtins.input', side_effect=user_input):
            stacks = sentence_output_input(sentence='')
        self.assertEqual(stacks[1], 'Баклан жуть крепово')

    def test_time_count(self):
        """Вывод времени работает верно"""
        with patch('builtins.input', side_effect=' '):
            stacks = sentence_output_input(sentence='')
        self.assertEqual(stacks[0], 0.0)


if __name__ == '__main__':
    unittest.main()
