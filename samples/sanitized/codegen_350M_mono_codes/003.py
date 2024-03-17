from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Aapko ek list di gayi hai jisme bank account ke deposit aur withdrawal operations hain, jiska shuruat zero balance se hota hai. Aapka task hai detect karna ki kya kisi bhi point pe account ka balance zero se kam ho jata hai, aur us point pe function ko True return karna chahiye. Varna ise False return karna chahiye.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    result = False
    if (operations[0] + operations[2] + operations[3] == 0) or (
        operations[0] + operations[1] + operations[3] < 0
    ):
        result = True
    elif operations[2] > 0:
        result = False
    return result