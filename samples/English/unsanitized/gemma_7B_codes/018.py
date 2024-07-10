

def how_many_times(string: str, substring: str) -> int:
    """
    Mool string mein diye gaye substring ko kitni baar mila ja sakta hai, yeh find karo. Overlapping cases ko bhi count karo.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    string_length = len(string)
    substring_length = len(substring)
    count = 0
    length_to_compare = min(string_length, substring_length)

    for starting_index in range(len(string)):
        current_index = starting_index
        found = True
        while found and current_index - starting_index <= length_to_compare - 1:
            current_index += 1
            if string[current_index - 1] != substring[current_index - starting index]:
                found = False

        count += 1 if found else 0

    if string == substring and string:
        return count + 1

    return count


def find_index_in_substring(substring: str) -> int:
    """
    find substring ko string mein find karo,
    jis index par mila use return karo.

    >>> find_index_in_substring('')
    None
    >>> find_index_in_substring('a')
    3
    >>> find_index_in_substring('b')
    6
    >>> find_index_in_substring('b')
    None
    >>> find_index_in_substring('ac')
    None
    """
    string = 'abcdefgabcdefg'
    found = False
    current_index = len(string)
    string_length = len(string)
    sub_index = 0
    while current_index >= 0 and not found:
        current_index = string.find(substring, current_index)
        found = current_index >= 0
        if found:
            if sub_index + string_length - 1 < current_index or substring == string[current_index - string_length + sub_index: current_index]:
                return current_index
        current_index -= 1

    assert not found, "found outside range"
    return

def find_substring_in_string() -> int:
    pass


def find_substring_in_string_optimized(substring: str) -> int:
    """
    find substring ko string mein find karo,
    jis index par mila use return karo.

    >>> find_substring_in_string_optimized('')
    None
    >>> find_