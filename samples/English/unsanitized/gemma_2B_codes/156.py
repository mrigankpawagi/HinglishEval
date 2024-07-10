
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    numbers = [
        'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x',
        'xl', 'l', 'll', 'lxx', 'xli', 'xlii', 'cc', 'ccx', 'ccc',
        'cd', 'cdx', 'cdlxx', 'dccx', 'cdclxxx', 'dccxl', 'dccli',
        'd', 'dx', 'dl', '#i', '#ii', '#ri']

    roman = {number: '' for number in numbers}

    for number, roman_name in roman.items():
        roman = roman_name + roman[number]

    return roman


# TESTS
import unittest


class TestMethods(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    def test_error(self):
        """
        Tests if incorrect input returns None.
        """
        self.assertIsNone(int_to_mini_roman(21))


if __name__ == '__main__':
    unittest.main()
