from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Aapko ek list di gayi hai jisme bank account ke deposit aur withdrawal operations hain, jiska shuruat zero balance se hota hai. Aapka task hai detect karna ki kya kisi bhi point pe account ka balance zero se kam ho jata hai, aur us point pe function ko True return karna chahiye. Varna ise False return karna chahiye.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        else:
            balance -= operation
    return balance < 0


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; HAPPY DAYS!\n")
