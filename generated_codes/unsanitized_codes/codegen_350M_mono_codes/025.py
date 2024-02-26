from typing import List


def factorize(n: int) -> List[int]:
    """
    Diye gaye integer ke prime factors ki list return karo, order chhote se bade tak hona chahiye.
    Har ek factor ko utni baar list mein hona chahiye jitni baar wo factorization mein aata hai.
    Input number sabhi factors ka product hona chahiye
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    result = []
    for i in range(1, n//1 + 2):
        if n % i == 0:
            result.append(i)
    if len(result)!= 0:
        result.sort()

    return result


mul = int(input())

mulList = factorize(mul)

arr = []
while len(mulList)!= 0:
    for i in range(0, len(mulList)):
        arr = mulList + arr
        print(arr)

        arr = [int(m) for m in arr]
        print(arr)
        break
