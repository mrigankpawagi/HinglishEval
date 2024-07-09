from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Diye gaye python values ki list ko sirf integers ke liye filter karo
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    int_list = []
    for value_element in values:
        if isinstance(value_element, int):
            int_list.append(value_element)
    return int_list

<|python|>"""
.. module:: pypy
   :synopsis: This module does the heavy lifting.
"""
from utils.utils import get_logger

from utils.constants import TESTS_PATH

import os
import os.path
import pkgutil
import sys
import tarfile
import tempfile
import subprocess
import json

logger = get_logger("main.py")


#