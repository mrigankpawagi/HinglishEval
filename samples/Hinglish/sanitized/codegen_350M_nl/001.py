from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Is function ka input ek string hota hai jisme multiple groups hote hain nested parentheses ke. Aapka goal hai
    un groups ko alag alag strings me separate karna aur unki list return karni hai.
    Separate groups balanced hote hain (har open brace sahi se close hota hai) aur ek dusre ke andar nested nahi hote
    Input string me koi bhi spaces ko ignore karo.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    for item in paren_string.split():
        for i in xrange(0, len(item)):
            yield paren_string[i]
            yield i
            i % 2 = 0
            break
            for i in xrange(len(item)-1):
                yield item[i:-1]
                print ''
                break
                for i in xrange(len(item)-1):
                    yield item[i:i]
        for i, k in enumerate(item):
            tl = ('.')
            if k:
                tl = ('. ').join(k)
            yield