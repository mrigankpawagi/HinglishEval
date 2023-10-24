

def remove_vowels(text: str):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    assert type(text) == str, "invalid inputs" # $_CONTRACT_$
    return "".join(list(filter(lambda ch: ch not in "aeiouAEIOU", text)))



METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'
    assert candidate('abcdef') == 'bcdf'
    assert candidate('aaaaa') == ''
    assert candidate('aaBAA') == 'B'
    assert candidate('zbcd') == 'zbcd'


check(remove_vowels)