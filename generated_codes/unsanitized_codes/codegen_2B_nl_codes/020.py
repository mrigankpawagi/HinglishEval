from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert isinstance(numbers, list)
    assert len(numbers) >= 3
    assert all(isinstance(number, float) for number in numbers)

    def find_closest(number):
        if number < 0:
            return None
        elif number > 0:
            return number  # number == number
        else:
            mid_index = (number + 0.5) // 2
            return numbers[mid_index]


#    def find_closest(number):
#        if number < 0:
#            return None
#        elif number > 0:
#            return number  # number == number
#        else:
#            mid_index = (number + 0.5) // 2
#       