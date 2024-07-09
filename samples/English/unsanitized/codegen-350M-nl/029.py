from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [list(f) for f in strings]


MATCHER = '^'

__all__ = [
    'pattern',
    'pattern_regexp',
   'match',
   'regexp',
   'regexp_regexp',
  ]


class MatchObject(object):
    def __new__(cls, state: Dict[str, MatchObject]):
        new_state = state
        for state in cls.states:
            new_state[state] = new_state[state] or new_state[state]
        return new_state


class Pattern(MatchObject):
    __doc__ = [
        "Return the `pattern` for the given input string and the given state.\n"
        "To specify additional patterns, use the `pattern_regexp` attribute.\n"
        "This does the same as `pattern`, but also uses the `pattern_regexp` attribute to tell Python to use a replacement pattern instead.\n"
    ]

    def __init__(self, pattern: str, state: Optional[dict[str, MatchObject]], format_regexp: Pattern) -> bool:
        self._pattern = pattern
        self._state = state

        self._format_regexp = pattern_regexp

        # A