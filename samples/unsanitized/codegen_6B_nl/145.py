
def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    nums = list(nums)
    new_list = []
    for digit in nums[:]:
        digit *= -1
        if digit <= 0:
            continue
        if digit % 10 == 0:
            new_digit = digit % 10
        else:
            new_digit = digit
            digit = 0
        new_digit += 1
        if new_digit == 10:
            new_digit = 0
        new_digit += 1
        if new_digit == 10:
            digit = 0
        new_list.append(new_digit)

    if len(nums)!= len(new_list):
        print(new_list)

    return new_list

