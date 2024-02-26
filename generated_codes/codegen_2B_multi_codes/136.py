
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    a, b = None, None
    for number in lst:
        if b is None:
            if number < 0:
                a, b = number, None
            else:
                b = number
        else:
            if a < number and number >= 0:
                a, b = number, None
            elif a > number and b >= number:
                a, b = number, None
            elif a == number and b is None:
                b = number
    if a is not None:
        return (a, b)
    return (None, None)


class MyTest(unittest.TestCase):
    '''
    Tests for largest_smallest_integer function.
    '''
    def test_all_negative(self):
        '''
        Test that the function finds the smallest and biggest
        negative integers.
        '''
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([-1]), (None, -1))
        self.assertEqual(largest_smallest_integers([-2]), (-2, None))
        self.assertEqual(largest_smallest_integers([-4]), (-4, None))
        self.assertEqual(largest_smallest_integers([-5]), (-5, None))

    def test_all_positive(self):
        '''
        Test that the function finds the smallest and biggest
        positive integers.
        '''
        self.assertE