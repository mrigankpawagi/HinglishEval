

def fib(n: int):
    """
    n-th Fibonacci number return karo.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    test = fib(15)
    assert (test, 15) == (21, 55)

    test = fib(22)
    assert (test, 22) == (21, 55)

    test = fib(4)
    assert (test, 4) == (1, 1)

    test = fib(5)
    assert (test, 5) == (1, 1)

    test = fib(10007)
    assert (test, 10007) == (8137, 130107)
<|python|>import requests
import os
import json


import uuid
import time

import urllib

from functools import reduce

import urwid

## Import your modules for your tasks
##
from. import configuration
from.configuration import API_KEY, HOST, WINDOW_NAME
from. import colors_and_effects
from. import utils


#