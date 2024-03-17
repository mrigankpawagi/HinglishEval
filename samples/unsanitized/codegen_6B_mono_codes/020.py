from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    """
    TEST: Create a sorted version of the input list of numbers, e.g. [-5.0, -1.0, -2.0, -4.0, -1.2, -3.9] and then call find_closest_elements(nums).
    """

    # Replace this line with your code (use sorted() to make a sorted copy of the given list)
    nums = sorted(numbers)

    """
    TEST: Create a list of tuples consisting of two float numbers in descending order where the second element of the tuple is the absolute value of the first element;
    For example, if you pass [-5.0, -1.0, -2.0, -4.0, -1.2, -3.9] this list could be generated like [(5.0, 5.0), (4.0, 2.0), (1.0, 2.0), (2.0, 2.0), (1.2, 3.9), (3.9, 4.0)]

    The first test case has produced the following output:
    (5.0, 5.0)
    (4.0, 2.0)
    (1.0, 2.0)
    (2.0, 2.0)
    (1.2, 3.9)
    (