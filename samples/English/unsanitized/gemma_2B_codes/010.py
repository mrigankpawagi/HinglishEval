

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # longest palindrome that starts with given string
    palindrome_length = len(string)
    while palindrome_length % 2 == 0:
        if is_palindrome(string[palindrome_length//2:]):
            break
        palindrome_length -= 1

    # make the palindrome
    return string[:palindrome_length//2] + string[-palindrome_length//2:] + string


def is_valid_triplet(input_string: str, input_index: int) -> bool:
    """ Returns True if input_string contains the two indexes of a triplet (e.g. 0,1,2),
    and the triplet is non-empty.
    >>> is_valid_triplet('12345', 3)
    True
    >>> is_valid_triplet('cat', 3)
    True
    >>> is_valid_triplet('catac', 2)
    True
    >>> is_valid_triplet('catacat', 4)
    False
    >>> is_valid_triplet('', 5)
    False
    """
    if input_index > len(input_string)-1:
        return False
    output_string = input_string[input_index:]
    for i in range(len(input_string)/3):
        if output_string == input_string[i*3:(i+1)*3]:
            return True
    return False

def find_triplets(string: str) -> list[int]:
    """ Find all triplets in input_string containing a valid integer triplet.
    >>> find_triplets('aa123344')
    [[2, 3, 4], [1, 2, 3], [0, 1, 2]]
    >>> find_triplets('c3d3d0')
    [[0, 1, 2]]
    """
    output_triplets = []
    for i in range(len(string)): # len(output_triplets)
        if not is_valid_triplet(string[i:], i):
            for j in range(len(output_triplets)):
                if output_triplets[j][1]-output_triplets[j][0] <= output_tri