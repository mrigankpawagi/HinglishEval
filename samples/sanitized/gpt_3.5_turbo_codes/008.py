from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Diye gaye integer list ke liye, ek tuple return karo jismei list ke saare integers ka sum aur product ho.
    Empty list ke sum ko 0 aur product ko 1 ke barabar hona chahiye.
    """
    if not numbers:
        return (0, 1)
    sum_of_numbers = sum(numbers)
    product_of_numbers = 1
    for num in numbers:
        product_of_numbers *= num
    return (sum_of_numbers, product_of_numbers)
