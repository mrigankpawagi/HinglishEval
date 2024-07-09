
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    def count_string(s):
        """Return true if the number of odd digits within's' is odd."""
        return len([e for e in s if e in "0123456789"]) % 2 == 1

    odd_list = []
    for s in lst:
        if len(s) and not count_string(s) == 0:
            odd_list.append('the number of odd elements %d of the string %d "of the input".' % (len(s), s))
    return odd_list[1:-1]

And I can't figure out why. I feel like this should be so easy.

A:

