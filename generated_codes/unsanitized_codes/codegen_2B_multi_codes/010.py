

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    string = list(string)
    string[0], string[-1] = string[-1], string[0]
    return ''.join(string)


def solution():
    """ Implement the solution method for this problem.
    :rtype: int
    """
    n = int(input().strip())
    for _ in range(n):
        string = input().strip()
        length = len(string)

        print("{}\t{}".format(length, is_palindrome(string) == True))
        print("{}\t{}".format(length, make_palindrome(string)))


if __name__ == '__main__':
    solution()
