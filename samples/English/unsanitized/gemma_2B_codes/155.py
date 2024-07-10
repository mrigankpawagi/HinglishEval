
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Write your code here.

    int_num = str(abs(num))
    int_list = list(int_num)

    even = 0
    odd = 0
    for index, value in enumerate(int_list):
        if value == str(int(value) % 2):
            even += 1
        else:
            odd += 1

    return (even, odd)



if __name__== '__main__':
    print("Example:")
    print(even_odd_count(-34))
    print(even_odd_count(1984))

    assert even_odd_count(-34) == (1, 1), "Even/Odd wrong"
    assert even_odd_count(1984) == (1, 2), "Even/Odd wrong"
    # These "asserts" are used for self-checking and not for an auto-testing
    assert even_odd_count([-12, 279, -4]) == (0, 3), "Even/Odd wrong"
    assert even_odd_count(1984) == (1, 2), "Even/Odd wrong"
    assert even_odd_count[0]) == (3, 1), "You're almost there!"
    assert even_odd_count([3, 4, 7]) == (0, 2), "Even/Odd wrong"
    print("Coding complete? Click 'Check' to earn cool rewards!")
