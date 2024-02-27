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
    groups_list: List[str]=[]
    for x in paren_string:
        if x.isnumeric() or x in "()":
            groups_list.append(x)
        else:
            for y in groups_list:
                if y.islower():
                    y="("+ y + ")"
                else:
                    y= y+"("
            groups_list.append(y)
    return groups_list
<|python|>import pytest
import logging
from typing import IO

from pybz2_stream import Bzip2Stream
from pybz2_stream.compat import compat_open

from tests.stream import Stream


class TestBzip2Stream(Stream):
    stream = Bzip2Stream()


@pytest.fixture
