

def median(l: list):
    """
    List l ke elements ka median return karo.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    low = len(l) // 2
    mid = len(l) // 2 - (2 * low)
    return l[mid - low][0]


if __name__ == '__main__':
    """
    Test unitlities of list functions.
    """
    import doctest
    doctest.testmod(include_unittest=True)
<|python|>r"""
    Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015 John Viega
    Copyright (C) 2010, 2011 Matthew P. Burruss
    Copyright (C) 2010, 2011, 2012, 2013, 2014, 2015 Greg Landrum

    This file is part of numpy.
    
    numpy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    numpy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with numpy.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy

_examples = """

>>> abs(1.0 / numpy.var([1, 0, -1]))
array(0)
>>> abs(numpy.var([1, 0, -1]))
array(0)

>>> # 1 / abs(1.0)
array(0.50000000000000)


>>> # numpy.arctan(arr)
array([0.570893415, -0.5708934