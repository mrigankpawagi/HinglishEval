from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    summed: List[float] = []
    for num in sorted(numbers):
        if abs(num) <= threshold:
            summed.append(num)
    return sum(summed) == 0


test_cases = int(input())
for x_cases in range(test_cases):
    l, m = map(int, input().split())
    lns = list(map(int, input().split()))
    res = 0
    for i in range(l):
        summed = [0] + lns + [l-1] + [0] + lns + [0] + lns + [m-1]
        for j in range(3):
            if (i+j+1) > x_cases:
                #