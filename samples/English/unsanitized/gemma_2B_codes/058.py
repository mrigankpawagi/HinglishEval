

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(set(l1 + l2) - set(l1) - set(l2))


def main():
    print(common([1, 4, 3, 3, 3, 1], [1, 4, 3, 3, 3, 5]))

main()

def is_anagram(str1, str2):
	"""Check if two strings are anagrams. Return True if anagram, else return False."""
    if str1 == str2:
        return True
    string1 = str(str1.lower())
    string2 = str(str2.lower())
    if len(string1 != len(string2)):
        return False
    return common(string1, string2) == []


print(is_anagram("hello", "olleh"))
print(is_anagram("hello", 'el'))
print(is_anagram("hello", "hello"))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
