from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    order_of_removal_of_numbers = list()

    for number in numbers:
        if len(order_of_removal_of_numbers) == 0:
            order_of_removal_of_numbers.append(number)

        elif number == order_of_removal_of_numbers[0]:
            # todo: check only last element to remove
            order_of_removal_of_numbers.remove(number)
            # todo: check only last element to remove


        # todo: check only last element to remove
    return order_of_removal_of_numbers

    # todo: check only last element to remove
    # todo: check only last element to remove


