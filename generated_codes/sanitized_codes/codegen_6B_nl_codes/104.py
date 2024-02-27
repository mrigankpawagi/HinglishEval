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