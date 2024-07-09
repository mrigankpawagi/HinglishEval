

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    p_num = int(number)
    f_num = number - p_num
    if f_num == 0:
        return p_num

    f_num_list = []

    while f_num > 1:
        next = f_num // 10
        f_num = int(f_num) - next
        f_num_list.append(next)

    f_num_list.append(float(f_num))

    assert not f_num_list[0], f_num_list[0]

    return sum([(p_num + integer(f) * int(f)) / 10 for f, integer in
                zip(f_num_list, range(1, 10))])

# This function converts string to float
