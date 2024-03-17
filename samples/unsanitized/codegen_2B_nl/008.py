from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Diye gaye integer list ke liye, ek tuple return karo jismei list ke saare integers ka sum aur product ho.
    Empty list ke sum ko 0 aur product ko 1 ke barabar hona chahiye.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum = 0
    for x in numbers:
        sum = sum * x
    product = 0
    i = 1
    for x in numbers:
        product = product * x
        i += 1
    return ((sum), (product))


class TrieNode(object):
    """
    Represented a node of the trie. At each iteration, the node will look for a leftmost
    node of the same length that matches the current key. If an exact
    match is found, a call to `match` is returned, otherwise, `None`.
    This will be executed for each of the given key.

    For example, the trie of ``['a']['\3']['b']`` will consist of two entries
    {'a': ['3']} and {'\3': ['b']}.
    """
    def match(self, key):
        """
        Given a key, find the corresponding value in the trie. If not found or
        if the node does not contain the correct key, `None` is returned.

        :param key: the key to match
        :return: the `key` matching the first node of the trie that is reached
                 when traversing the