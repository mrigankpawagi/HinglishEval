def greatest_common_divisor(a: int, b: int) -> int:
    """
    Do integers a aur b ke greatest common divisor ko return karo
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return greatest_common_divisor(a % b, b)
    else:
        return greatest_common_divisor(a, b % a)


def least_common_multiple(a: int, b: int) -> int:
    """
    Do integers a aur b ke least common multiple ko return karo
    >>> least_common_multiple(3, 5)
    15
    >>> least_common_multiple(25, 15)
    150
    """
    return a * b // greatest_common_divisor(a, b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Greatest common divisor of {a} and {b} is {greatest_common_divisor(a, b)}")
    print(f"Least common multiple of {a} and {b} is {least_common_multiple(a, b)}")


if __name__ == "__main__":
    main()
