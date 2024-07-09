

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisibles = 1
    remainder = n
    n = remainder.copy()
    while not n == 1:
        if n % 2 == 0:
            divisibles += 1
        n = remainder // 5

        remainder = remainder.copy()

    return divisibles

if __name__ == "__main__":
    try:
        number = int(input())
        print(largest_divisor(number))
    except:
        exit('0')
