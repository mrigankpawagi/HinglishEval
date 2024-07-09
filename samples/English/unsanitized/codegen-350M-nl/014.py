from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    # for item in string:
    # if item.startswith(LATEST_PREFIX):
    #     result.append('prefer_all_prefixes' if item.startswith(LATEST_PREFIX) else '')
    strings = re.findall(r'\(.*\)', string)
    if not all(len(items) for items in strings):
        return result

    def is_preferred_prefix(l: str) -> bool:
        return is_preferred_word(l) and all_prefixes(l)!= ''
    return [item for item in items if item.endswith('.prefixes')]


