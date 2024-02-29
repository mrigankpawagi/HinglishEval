
def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    return sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))


# 2
def order_by_length(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka length ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka length similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_length([1, 11, -1, -11, -12]) == [-1, -11, -12, 1, 11]
    >>> order_by_length([]) == []
    """
    return sorted(nums, key=lambda x: (len(str(x)), nums.index(x)))


# 3
def order_by_digits(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_digits([1, 11, -1, -11, -12]) == [-1, -11, -12, 1, 11]
    >>> order_by_digits([]) == []
    """
    return sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))


# 4
def order_by_digits_length(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ke length ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ke length similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_digits_length([1, 11, -1, -11, -12]) == [-1, -11, -12, 1, 11]
    >>> order_by_digits_length([])