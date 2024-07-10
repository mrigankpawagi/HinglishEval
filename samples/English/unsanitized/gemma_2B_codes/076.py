
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    return x == n**int(math.log(x, n))


def count_simple_powers(n, number, prime_list, simple_power_value):
    if number == 1:
        return 1
    prime_list.append(number)
    possible_power = int(math.ceil(number / n) * n)
    if not possible_power >= number:
        number -= 1

    for _ in range(possible_power - number, 0, -1):
        sub_prime_list = prime_list[:]
        sub_simple_power_value = (possible_power - number)
        count_simple_powers(n, number + sub_simple_power_value, sub_prime_list, sub_simple_power_value)

    return len(prime_list)


def main(n):
    if not type(n) == int:
        raise TypeError("Input should be a number")

    prime_list = list()
    count_simple_powers(n, 1, prime_list, 1)
    for value in prime_list:
        print(value)

    print(4, count_simple_powers(10, 10, [], 0))


if __name__ == '__main__':
    main(3)
