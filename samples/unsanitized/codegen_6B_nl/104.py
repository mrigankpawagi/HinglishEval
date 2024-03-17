
def unique_digits(x):
    """
    Diye gaye positive integers ki list x me Woh saare elements ki sorted list return karo jisme koi bhi even digit nahi hai.

    Dhyan de: Return ki gayi list ko increasing order me sort kiya jana chahiye.
    
    Jaise ki:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    x = list(int(x))

    # list of all even digits in the number
    even_digits = set()

    for i, number in enumerate(x):
        if number % 2 == 0 and number not in even_digits:
            even_digits.add(number)
            x.pop(i)

    # sort according the numbers of even digits
    x.sort(key=lambda x: len(even_digits))

    output = [number for number in x]
    output.append(x.pop(0))

    return output


# Python 2:
#    List of all (odd-positive) prime numbers below 1000
#    Python 2:
#        >>> from sys import set_precision
#        >>> prime_numbers = set_precision(1000)
#        >>> list(prime_numbers)
#        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193