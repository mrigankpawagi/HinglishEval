from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Aapko ek list di gayi hai jisme bank account ke deposit aur withdrawal operations hain, jiska shuruat zero balance se hota hai. Aapka task hai detect karna ki kya kisi bhi point pe account ka balance zero se kam ho jata hai, aur us point pe function ko True return karna chahiye. Varna ise False return karna chahiye.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """

    if not operations:
        return False

    zero = sum(operations)

    if zero > 0:
        return zero < operations[0] * -1
    return True