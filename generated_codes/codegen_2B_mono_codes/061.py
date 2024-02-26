

def correct_bracketing(brackets: str):
    """
    brackets ek string hai "(" aur ")" ka.
    return True agar har opening bracket ka ek corresponding closing bracket ho.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    count = 0
    for open_ in brackets:
        try:
            pairs = brackets_dict[open_]
        except KeyError:
            print("Wrong bracket!!!")
            return False
        try:
            count += 1
            count += pairs[open_]
        except TypeError:
            continue

    count -= 1

    return count == 0

if __name__ == "__main__":
    print(correct_bracketing("(") is False)
    print(correct_bracketing("()") is True)
    print(correct_bracketing("(()())") is True)
    print(correct_bracketing(")(()") is False)

    n = int(input("Enter the number of brackets : "))
    print("Brackets :")
    print("Brackets:")
    while n:
        ch = input()
        print(correct_bracketing(ch))
        n -= 1
