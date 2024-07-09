from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    from nba import mlb
    return [mlb.Mlb_MlbWordInfo.prefix(mlb.get_mlb_word(string)) for string in mlb.get_mlb_words(string)]


