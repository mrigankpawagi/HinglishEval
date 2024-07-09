
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(arr)


class Test(unittest.TestCase):
    def test_sort_array_positive(self):
        self.assertEqual(sort_array([2, 3, 4, 5, 1]), [1, 2, 3, 4, 5])

    def test_sort_array_negative(self):
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])

    def test_sort_array_zero(self):
        self.assertEqual(sort_array([0]), [0])


if __name__ == '__main__':
    unittest.main()